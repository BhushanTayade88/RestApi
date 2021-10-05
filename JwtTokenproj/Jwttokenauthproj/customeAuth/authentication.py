from django.contrib.auth import get_user_model,authenticate
from rest_framework import exceptions
from rest_framework import authentication
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class CustomeAuthentication(BaseAuthentication):
    # def authenticate(self, request):
    #     username = request.data['username']
    #     print(username)
    #     if username is None:
    #         return None
    #     try:
    #         user = User.objects.get(username=username)
    #     except User.DoesNotExist():
    #         raise AuthenticationFailed("No such type of user")

    #     return(user,None)
  

    def authenticate(self, request):

        # Get the username and password
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        if not username or not password:
            raise exceptions.AuthenticationFailed('No credentials provided.')

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed('Invalid username/password.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')


        return (user, None) 