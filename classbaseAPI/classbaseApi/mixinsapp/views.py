
from django.shortcuts import render
from rest_framework import mixins,generics, status
from rest_framework.response import Response
from .models import Course2,Course2Serializers
from rest_framework.viewsets import ModelViewSet, ViewSet

# Create your views here.
'''
class CourseListview(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Course2.objects.all()
    serializer_class = Course2Serializers
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class CourseDetailsView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Course2.objects.all()
    serializer_class = Course2Serializers

    def get(self,request,pk):
        return self.retrieve(request, pk)
    def put(self,request,pk):
        return self.update(request, pk)
    def delete(self,request,pk):
        return self.destroy(request, pk)
  '''  

  # Generic methods without mixins
'''
class CourseListview(generics.ListAPIView,generics.CreateAPIView):
    queryset = Course2.objects.all()
    serializer_class = Course2Serializers
class CourseDetailsView(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Course2.objects.all()
    serializer_class = Course2Serializers
'''
'''
class CourseListview(generics.ListCreateAPIView):
    queryset = Course2.objects.all()
    serializer_class = Course2Serializers
class CourseDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course2.objects.all()
    serializer_class = Course2Serializers
'''

# View sets
'''
class CourseListview(ViewSet):
    def list(self,request):
        course = Course2.objects.all()
        serializer = Course2Serializers(course, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = Course2Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def retrive(self,request,pk):
        try:
            course = Course2.objects.get(pk = pk)
        except Course2.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = Course2Serializers(course)
        return Response(serializer.data)   
'''



class CourseListview(ModelViewSet):
    queryset = Course2.objects.all()
    serializer_class = Course2Serializers