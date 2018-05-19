from django.contrib import admin
from django.conf.urls import url, include
from models_test import views

app_name = 'models_test'

urlpatterns = [
    url(r'^$', views.contacts, name='contacts'),
    url(r'^create/', views.create_contact, name='create_contact'),
    url(r'^delete/(?P<contact_id>\d+)/$', views.delete_contact, name='delete_contact'),
    url(r'^edit/(?P<contact_id>\d+)/$', views.edit_contact, name='edit_contact'),
    url(r'^get/(?P<contact_id>\d+)/$', views.contact, name='contact'),
    url(r'^google_auth/', include('google_auth.urls')),
    url(r'^delete/all/$', views.delete_all_contacts, name='delete_all_contacts'),
    url(r'^filter/country/$', views.filter_by_country, name='filter_by_country'),
    url(r'^filter/city/$', views.filter_by_city, name='filter_by_city'),
    url(r'^filter/job/$', views.filter_by_job, name='filter_by_job')
]
