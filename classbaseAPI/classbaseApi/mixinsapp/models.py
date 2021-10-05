from django.db import models

# Create your models here.
class Course2(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    discount = models.FloatField()
    duration = models.IntegerField()
    authername = models.CharField(max_length=30)


from rest_framework import serializers

class Course2Serializers(serializers.ModelSerializer):

    class Meta:
        model = Course2
        fields = '__all__'