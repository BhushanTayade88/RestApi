from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student,StudentSerializer
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated
from .authentication import CustomeAuthentication
# Create your views here.
class StudentCRUD(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomeAuthentication]
    permission_classes = [IsAdminUser]