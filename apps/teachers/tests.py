from django.test import TestCase
from rest_framework.test import APIClient
from .models import Teacher
from apps.courses.models import Course

class TeacherModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name="Math", code="MTH101")
        self.teacher = Teacher.objects.create(
            first_name="John",
            last_name="Smith",
            email="john.smith@example.com",
            subject="Math",
            date_of_birth="1980-01-01",
            course=self.course
        )

    def test_teacher_creation(self):
        self.assertEqual(self.teacher.first_name, "John")
        self.assertEqual(self.teacher.subject, "Math")
        self.assertEqual(self.teacher.course.name, "Math")

class TeacherAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(name="Math", code="MTH101")
        self.teacher = Teacher.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            subject="Science",
            date_of_birth="1990-01-01",
            course=self.course
        )

    def test_teacher_api(self):
        response = self.client.get('/api/teachers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
