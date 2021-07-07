from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.parsers import JSONParser
from .serializers import StudentSerializers
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# Create your views here.
@csrf_exempt
def empview(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        serializer = StudentSerializers(stu,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        jsondata = JSONParser().parse(request)
        print(jsondata)
        serializer = StudentSerializers(data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'data saved succesfully'})
        else:
            return JsonResponse(serializer.errors, safe=False)

@csrf_exempt
def StudentDetailview(request,pk):

    try:
        student = Student.objects.get(pk = pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "DELETE":
        student.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    elif request.method =="GET":
        serializer = StudentSerializers(student)
        return JsonResponse(serializer.data,safe=False)
    elif request.method =="PUT":
        jsondata = JSONParser().parse(request)
        serializer = StudentSerializers(student,data=jsondata)
        print(jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)


