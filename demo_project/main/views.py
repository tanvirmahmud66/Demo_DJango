from django.shortcuts import render
from main.models import Students
# Create your views here.
def main(request):
    value = {"name": "Tanvir Mahmud Fahim"}
    return render(request, 'main/main.html', context = value)


def student_info(request):
    pupils = Students.objects.all()
    dictionaries = {
        "students": pupils,
    }
    return render(request, 'main/student.html', context=dictionaries)

