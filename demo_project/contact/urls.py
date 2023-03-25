from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('fillcontact', views.input_form, name='add_contact'),
]