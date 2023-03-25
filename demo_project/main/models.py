from django.db import models

# Create your models here.
class Students(models.Model):
    student_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=30)
    student_batch = models.IntegerField()
