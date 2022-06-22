from statistics import mode
from django.db import models

# Create your models here.

class Student(models.Model):
    F_name = models.CharField(max_length=40)
    L_name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
