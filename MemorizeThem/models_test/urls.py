from django.contrib import admin
from django.conf.urls import url
from models_test import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
