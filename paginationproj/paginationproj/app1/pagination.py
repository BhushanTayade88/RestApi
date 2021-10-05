from rest_framework.pagination import *

class EmployeePagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'mypage'
    page_size_query_param = 'client'
    max_page_size = 20
    

class EmployeeOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 20

class EmployeeCursorPagination(CursorPagination):
    page_size=10
    ordering='empname'
    # cursor_query_param='cu'