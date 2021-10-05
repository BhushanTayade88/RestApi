
from .models import Course3,Instructor
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course3
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True,read_only=True)
    class Meta :
        model = Instructor
        fields = '__all__'