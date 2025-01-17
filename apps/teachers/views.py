from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    search_fields = ['first_name', 'last_name', 'email', 'subject']
    filterset_fields = ['course']
