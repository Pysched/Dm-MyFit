from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactus_form, name='contactus')
]