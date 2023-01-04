from django.contrib import admin
from . models import Contact , Testimoniall

admin.site.register(Contact)
admin.site.register(Testimoniall)

# Register your models here.


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('course_name' , 'available' , 'teacher')
#     list_filter = (
#         ('available' , admin.BooleanFieldListFilter),
#     )
#     search_fields = ['course_name']
