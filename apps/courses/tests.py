from django.test import TestCase
from rest_framework.test import APIClient
from .models import Course

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name="Mathematics",
            code="MTH101",
            description="Introduction to Mathematics",
            credits=3
        )

    def test_course_creation(self):
        self.assertEqual(self.course.name, "Mathematics")
        self.assertEqual(self.course.credits, 3)

class CourseAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(
            name="Science",
            code="SCI101",
            description="Introduction to Science",
            credits=4
        )

    def test_course_api(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
