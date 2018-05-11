from django.conf.urls import url
from django.urls import include
from user_authorization import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^registration/', views.registration, name='registration')
]
