from django.contrib import admin
from .models import Course , Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name' , 'available' , 'teacher')
    list_filter = (
        ('available' , admin.BooleanFieldListFilter),
    )
    search_fields = ['course_name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug':('name',) }



# Register your models here.
