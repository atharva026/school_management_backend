from celery import shared_task
from django.core.mail import send_mail
from .models import Course

@shared_task
def send_course_creation_notification(course_id):
    course = Course.objects.get(id=course_id)
    send_mail(
        'New Course Created!',
        f'A new course "{course.name}" has been added to the catalog.',
        'admin@school.com',
        ['admin@school.com'],
        fail_silently=False,
    )
