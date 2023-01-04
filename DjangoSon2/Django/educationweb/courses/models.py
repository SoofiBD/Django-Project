from django.db import models
from teachers.models import Teacher
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50 , null=True)
    slug = models.SlugField(max_length=50 , unique=True , null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    teacher = models.ForeignKey(Teacher , null=True , on_delete=models.CASCADE)
    course_name = models.CharField(max_length=30 , unique=True)
    category = models.ForeignKey(Category , null=True , on_delete = models.DO_NOTHING)
    students = models.ManyToManyField(User , blank=True , related_name='courses_joined')
    course_detail = models.TextField(blank=True)
    course_img = models.ImageField(upload_to="courses/%Y/%m/%d/" , default="courses/static/img/courses-1.jpg" , blank=True) ### /img
    date = models.DateField(auto_now=True)
    available = models.BooleanField(default=True)
    rating = models.IntegerField(default = True)
    Language = models.CharField(max_length=30 , default='English')
    course_price = models.CharField(max_length=10 , default='Free')
    skill_level= models.CharField(max_length=50 , default='All Level')
    
    def __str__(self):
        return self.course_name
# Create your models here.
