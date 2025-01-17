from django.db import models
from django.utils import timezone
from apps.courses.models import Course  

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    registration_date = models.DateTimeField(default=timezone.now)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Property to calculate age from date_of_birth
    @property
    def age(self):
        today = timezone.now().date()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
        return age

    class Meta:
        indexes = [
            models.Index(fields=['email']),
        ]