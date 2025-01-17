from rest_framework import serializers
from .models import Teacher
from apps.courses.models import Course 

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'code']

class TeacherSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'email', 'subject', 'date_of_birth', 'hire_date', 'course', 'age']
