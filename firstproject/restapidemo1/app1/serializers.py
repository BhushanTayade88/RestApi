from .models import Student
from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    phone = serializers.CharField(max_length=20)

    def create(self, validated_data):
        print('create method called')
        return Student.objects.create(**validated_data)

    def update(self, student, validated_data):
        newstudent = Student(**validated_data)
        newstudent.id = student.id
        newstudent.save()
        return newstudent