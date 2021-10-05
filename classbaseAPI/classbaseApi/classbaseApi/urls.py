
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from mixinsapp.views import CourseListview
from nestedser.views import InstructorListView,CourseListView
router = DefaultRouter()
router1 = DefaultRouter()
router2 = DefaultRouter()
router.register('courses',CourseListview, basename='course')
router1.register('instructor',InstructorListView, basename='instructors')
router2.register('course3',CourseListView, basename='courses')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/',include('CVBapp.urls')),
    path('mixins/',include(router.urls)),
    path('instru/',include(router1.urls)),
    path('course/',include(router2.urls)),
    # path('mixins/',include('mixinsapp.urls'))

]
