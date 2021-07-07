from django.urls import path
from . import views
urlpatterns  = [
    path('',views.empview),
    path('pkop/<int:pk>/',views.StudentDetailview)
 ]


