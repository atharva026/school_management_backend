from celery import shared_task
from django.core.mail import send_mail
from .models import Student

@shared_task
def send_welcome_email(student_id):
    student = Student.objects.get(id=student_id)
    send_mail(
        'Welcome to Our School!',
        f'Hi {student.first_name} {student.last_name},\n\nThank you for registering with us!',
        'admin@school.com',
        [student.email],
        fail_silently=False,
    )