from re import S
from rest_framework.viewsets import ModelViewSet
from .models import Course3, Instructor
from django.shortcuts import render
from rest_framework import generics
from .serializer import CourseSerializer,InstructorSerializer
# Create your views here.
class InstructorListView(ModelViewSet):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class CourseListView(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course3.objects.all()