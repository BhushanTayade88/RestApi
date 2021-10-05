from django.http.response import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course,CourseSerializers


class CourseListView(APIView):
    def get(self,request):
        course = Course.objects.all()
        serializer = CourseSerializers(course,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class CourseDetailView(APIView):
    def get_course(self, pk):
        try:
            return Course.objects.get(pk = pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        course = self.get_course(pk)
        serializer = CourseSerializers(course)
        return Response(serializer.data)
    def put(self, request,pk):
        course = self.get_course(pk)
        serializer = CourseSerializers(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request,pk):
        course = self.get_course(pk)
        course.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
