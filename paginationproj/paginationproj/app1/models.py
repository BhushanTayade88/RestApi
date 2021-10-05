from django.db import models


# Create your models here.
class Employee(models.Model):
    empid = models.CharField(max_length=50)
    empname = models.CharField(max_length=50)
    empsal = models.FloatField()
    empaddr = models.TextField(max_length=250)
