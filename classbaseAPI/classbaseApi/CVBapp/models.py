from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    discount = models.FloatField()
    duration = models.IntegerField()
    authername = models.CharField(max_length=30)


from rest_framework import serializers

class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'