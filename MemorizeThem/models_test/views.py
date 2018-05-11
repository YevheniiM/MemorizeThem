from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from models_test.models import Contact
from django.contrib import auth


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for
    # example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'contacts': Contact.objects.all()}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('index.html', context_dict)


def contacts(request):
    return render_to_response('contacts.html', {'contacts': Contact.objects.all(),
                                                'user': auth.get_user(request)})


def contact(request, contact_id=1):
    return render_to_response('contact.html', {'contact': Contact.objects.get(id=contact_id),
                                               'user': auth.get_user(request)})


