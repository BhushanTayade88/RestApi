from . import views
from django.urls import path

urlpatterns = [
    path('course', views.CourseListView.as_view()),
    path('course/<int:pk>', views.CourseDetailView.as_view())
]