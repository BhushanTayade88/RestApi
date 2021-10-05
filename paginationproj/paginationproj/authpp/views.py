from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .permissions import IsReadOnly,IsGetPostOrPut
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

#create tokens for all user
# users = User.objects.all()
# for user in users:
#     token = Token.objects.get_or_create(user=user)

class StudentCRUD(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAdminUser,IsGetPostOrPut,]