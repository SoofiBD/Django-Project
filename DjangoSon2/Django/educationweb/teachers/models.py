from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=50 )
    tatle = models.CharField(max_length=50 )
    image = models.ImageField(upload_to="courses\%Y\%m\%d" , default="courses/static/img/courses-1.jpg" , blank=True )
    facebook = models.URLField(max_length=150 , blank=True)
    instagram = models.URLField(max_length=150 , blank=True)
    twitter = models.URLField(max_length=150 , blank=True)
    linkedin = models.URLField(max_length=150 , blank=True)

    def __str__(self):
        return self.name

# Create your models here.
