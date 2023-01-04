from django.db import models
from courses.models import Course
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Testimoniall(models.Model):
    course_done = models.ForeignKey(Course , null=True , on_delete=models.DO_NOTHING)
    std_name = models.ForeignKey(User , null=False , on_delete=models.DO_NOTHING)
    comment = models.TextField()
 
    def __int__(self):
        return self.course_done 


# Create your models here.
