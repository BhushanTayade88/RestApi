from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password','phone']
admin.site.register(Student,StudentAdmin)