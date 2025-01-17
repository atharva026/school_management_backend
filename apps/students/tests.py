from django.test import TestCase
from rest_framework.test import APIClient
from .models import Student
from apps.courses.models import Course

class StudentModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name="Mathematics", code="MTH101")
        self.student = Student.objects.create(
            first_name="John",
            last_name="Smith",
            email="john.smith@example.com",
            date_of_birth="2000-01-01"
        )
        self.student.courses.add(self.course)

    def test_student_creation(self):
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.courses.first().name, "Mathematics")
        self.assertEqual(self.student.age, 25)  
        
class StudentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(name="Science", code="SCI101")
        self.student = Student.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            date_of_birth="1995-01-01"
        )
        self.student.courses.add(self.course)

    def test_student_api(self):
        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
