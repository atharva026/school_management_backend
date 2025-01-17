from rest_framework import serializers
from apps.courses.models import Course
from apps.students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'registration_date', 'courses']
