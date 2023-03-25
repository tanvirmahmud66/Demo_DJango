from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
