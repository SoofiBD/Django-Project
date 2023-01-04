from datetime import date
from django.shortcuts import render
from . models import Course , Category
from teachers.models import Teacher
from django.shortcuts import get_object_or_404


def courses(request , category_slug=None):
    category_page = None
    categories = categories = Category.objects.all()

    if category_slug != None:
        category_page = get_object_or_404(Category , slug = category_slug)
        courselist = Course.objects.filter(available=True,category=category_page)

    else:
       courselist = Course.objects.all().order_by('-date') 

    context = {
        'courselist':courselist,
        'categories':categories
    }
    return render(request, "courses.html" , context)



def details(request , category_slug , course_id):
    course = Course.objects.get(category__slug = category_slug , id = course_id)
    categories = Category.objects.all()
    courselist = Course.objects.all().order_by('-date')[:4]
    context = {
        'course' : course,
        'courselist':courselist,
        'categories':categories
    }
    return render(request, "details.html" , context)


def search(request):
    courselist = Course.objects.filter(course_name__contains = request.GET['search'])
    categories = Category.objects.all()

    context = {
        'courselist':courselist,
        'categories' : categories
    }

    return render(request , 'courses.html' , context)

