from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('student', views.student_info, name='students'),
]