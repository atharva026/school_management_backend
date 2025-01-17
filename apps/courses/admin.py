from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'credits')
    search_fields = ('name', 'code')
    list_filter = ('credits',)
