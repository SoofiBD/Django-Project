from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<slug:category_slug>/<int:course_id>', views.details, name='details'),
    path('categories/<slug:category_slug>', views.courses, name='category_details'),
    path('search/' , views.search , name='search'),
    
]
# from djangoo.http import HTTPResponse
