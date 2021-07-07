from django.urls import path
from . import views
urlpatterns  = [
    path('course',views. courselistview),
    path('course/<int:pk>',views. coursedetailview)
 ]