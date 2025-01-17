from django.db import models
from django.utils import timezone
from apps.courses.models import Course 

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    hire_date = models.DateTimeField(default=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return timezone.now().year - self.date_of_birth.year

    class Meta:
        indexes = [
            models.Index(fields=['email']),
        ]
