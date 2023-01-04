from django.urls import path
from . import views
from eduapp.views import IndexView , AboutView , ContactView


urlpatterns = [
    path('', IndexView.as_view() , name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('testimonial.html/',views.testimonial , name='testimonial'),
    path('feature.html',views.feature , name='feature')
]
# from djangoo.http import HTTPResponse
# from django.views.generic import TemplateView
# from django.shortcuts import render