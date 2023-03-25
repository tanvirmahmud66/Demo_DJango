from django.contrib import admin
from main.models import Students

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_id', 'student_batch')
admin.site.register(Students, StudentAdmin)
