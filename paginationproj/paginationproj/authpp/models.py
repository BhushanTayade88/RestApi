from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.CharField(max_length=50)
    stname = models.CharField(max_length=50)
    stmarks = models.FloatField()
    staddr = models.TextField(max_length=250)