from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from models_test.models import Contact, ContactForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def title(request):
    return render(request, 'title.html')


@login_required(login_url='/auth/login/')
def contacts(request):
    return render_to_response('contacts.html', {'contacts': Contact.objects.filter(owner_id=auth.get_user(request).id),
                                                'user': auth.get_user(request)})


def contact(request, contact_id=1):
    return render_to_response('contact.html', {'contact': Contact.objects.get(id=contact_id),
                                               'user': auth.get_user(request)})


def delete_contact(request, contact_id):
    Contact.objects.filter(id=contact_id).delete()
    return redirect('/contacts/')


def delete_all_contacts(request):
    Contact.objects.filter(owner_id=auth.get_user(request).id).delete()
    return redirect('/contacts/')


@login_required(login_url='/auth/login/')
def create_contact(request):
    if request.POST:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner_id = auth.get_user(request).id
            instance.save()
            return redirect('models_test:contacts')
    else:
        form = ContactForm()

    return render(request, 'create_contact.html', {'form': form})


@login_required(login_url='/auth/login/')
def edit_contact(request, contact_id):
    if request.POST:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            print(contact_id)

            contact = Contact.objects.get(id=contact_id)
            contact.id = contact_id
            contact.name = form.cleaned_data['name']
            contact.surname = form.cleaned_data['surname']
            contact.patronymic = form.cleaned_data['patronymic']
            contact.country = form.cleaned_data['country']
            contact.city = form.cleaned_data['city']
            contact.flat_number = form.cleaned_data['flat_number']
            contact.house_number = form.cleaned_data['house_number']
            contact.email = form.cleaned_data['email']
            contact.mobile_phone = form.cleaned_data['mobile_phone']
            contact.work_phone = form.cleaned_data['work_phone']
            contact.home_phone = form.cleaned_data['home_phone']
            contact.job = form.cleaned_data['job']
            contact.biography = form.cleaned_data['biography']
            contact.interests = form.cleaned_data['interests']
            contact.photo = form.cleaned_data['photo']

            contact.save()

            return redirect('models_test:contacts')
    else:
        contact = Contact.objects.get(id=contact_id)
        data = {
            'name': contact.name,
            'surname': contact.surname,
            'patronymic': contact.patronymic,
            'country': contact.country,
            'city': contact.city,
            'flat_number': contact.flat_number,
            'house_number': contact.house_number,
            'email': contact.email,
            'mobile_phone': contact.mobile_phone,
            'work_phone': contact.work_phone,
            'home_phone': contact.home_phone,
            'job': contact.job,
            'biography': contact.biography,
            'interests': contact.interests,
            'photo': contact.photo,
        }
        form = ContactForm(initial=data)

    return render(request, 'edit_contact.html', {'form': form,
                                                 'contact_id': contact_id})


def filter_by_city(request):
    if request.POST:
        data = request.POST.get('filter_field')
        print(data)
        return render(request, 'contacts.html', {'city': data,
                                                 'contacts': Contact.objects.filter(owner_id=auth.get_user(request).id)})
    else:
        return render(request, 'filter.html', {'contacts': Contact.objects.filter(owner_id=auth.get_user(request).id)})


def filter_by_country(request):
    if request.POST:
        data = request.POST.get('filter_field')
        print(data)
        return render(request, 'contacts.html', {'country': data,
                                                 'contacts': Contact.objects.filter(owner_id=auth.get_user(request).id)})
    else:
        return render(request, 'filter.html', {'contacts': Contact.objects.filter(owner_id=auth.get_user(request).id)})


def filter_by_job(request):
    if request.POST:
        data = request.POST.get('filter_field')
        print(data)
        return render(request, 'contacts.html', {'job': data,
                                                 'contacts': Contact.objects.filter(owner_id=auth.get_user(request).id)})
    else:
        return render(request, 'filter.html', {'contacts': Contact.objects.filter(owner_id=auth.get_user(request).id)})
