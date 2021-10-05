from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField(default=0)
    stname= models.CharField(max_length=50)
    stmarks= models.FloatField()
    staddr = models.TextField(max_length=250)

from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'