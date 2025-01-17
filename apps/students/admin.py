from django.contrib import admin
from .models import Student
from apps.courses.models import Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'registration_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('courses',)
