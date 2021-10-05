
from django.contrib import admin
from django.urls import path,include
from app1.views import EmployeeListView,EmployeeOffsetView,EmployeeCursorView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from authpp.views import StudentCRUD

router = DefaultRouter()
router.register('auth',StudentCRUD)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/',EmployeeListView.as_view()),
    path('emp2/',EmployeeOffsetView.as_view()),
    path('emp3/',EmployeeCursorView.as_view()),
    path('authapp/',include(router.urls)),
    path('get-api-token/',views.obtain_auth_token,name='get_auth_token'),
]
 