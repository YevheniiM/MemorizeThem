from django.contrib import admin
from django.conf.urls import url
from models_test import views

urlpatterns = [
    url(r'^$', views.contacts, name='contacts'),
    url(r'^contacts/all/$', views.contacts, name='contacts'),
    url(r'^contacts/get/(?P<contact_id>\d+)/$', views.contact, name='contact'),

]
