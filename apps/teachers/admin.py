from django.contrib import admin
from .models import Teacher
from apps.courses.models import Course

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email', 'subject')
    list_filter = ('course',)