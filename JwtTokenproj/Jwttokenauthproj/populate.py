
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Jwttokenauthproj.settings')
import django
django.setup()
from random import *
from faker import Faker 
from customeAuth.models import Student

fake = Faker()

def populate(n):
    for i in range(n):
        # print('empid',randint(100,999))
        # print('empname',fake.name())
        # print('empsal',randint(1000000,35000000))
        # print('empaddr',fake.city())
        #Employee.objects.create(empid=empid,empname=empname,empsal=empsal,empaddr=empaddr)
        empid=randint(100,999)
        empname = fake.name()
        empsal = randint(1,99)
        empaddr = fake.city()
        Student.objects.create(rollno=empid,stname=empname,stmarks=empsal,staddr=empaddr)

populate(150)
