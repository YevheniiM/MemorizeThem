from django.conf.urls import url
from google_auth import views

urlpatterns = [
    url(r'^sync/', views.login, name='login'),
]