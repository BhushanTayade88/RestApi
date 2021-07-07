
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import  status
from .models import Course,CourseSerializers


@api_view(['GET','POST'])
def courselistview(request):
    if request.method == 'GET':
        course = Course.objects.all()
        serializer = CourseSerializers(course,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        

@api_view(['GET','PUT','DELETE'])
def coursedetailview(request,pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CourseSerializers(course)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = CourseSerializers(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
    elif request.method =='DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
