from django.shortcuts import redirect
from .core import contacts as cont
from .core import quickstart
from models_test.models import Contact
from django.contrib import auth
import os


def login(request):
    c = quickstart.Connections()
    users = c.get_all_data()
    contacts = cont.Contacts(users).contacts
    for contact in contacts:
        s1 = Contact.objects.filter(mobile_phone=contact.phone_number.get('phone', -1),
                                    owner_id=auth.get_user(request).id)
        s2 = Contact.objects.filter(email=contact.email,
                                    owner_id=auth.get_user(request).id)

        if not s1 and not s2:
            con = Contact()
            con.owner_id = auth.get_user(request).id
            con.name = contact.name
            con.email = contact.email
            con.mobile_phone = contact.phone_number.get('phone', '')
            con.photo = contact.photos
            con.save()

    c.del_credentials()

    return redirect('/contacts/')
