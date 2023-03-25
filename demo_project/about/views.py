from django.shortcuts import render
from about.models import Teacher

# Create your views here.
def about(request):
    return render(request, 'about/about.html')


def teacher_info(request):
    teacher = Teacher.objects.all()
    dictonaries = {
        "teacher": teacher
    }
    return render(request, 'about/teacher.html', context=dictonaries)
