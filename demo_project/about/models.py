from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.IntegerField()
    teacher_name = models.CharField(max_length=40)
    teacher_email = models.CharField(max_length=40)