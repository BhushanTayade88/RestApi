from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudenteAdmin(admin.ModelAdmin):
    list_display=['rollno','stname','stmarks','staddr']