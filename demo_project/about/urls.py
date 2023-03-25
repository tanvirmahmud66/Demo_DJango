from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name='about'),
    path('teacher', views.teacher_info, name='teachers'),
]
