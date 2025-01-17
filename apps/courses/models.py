from django.db import models
from django.core.validators import MinValueValidator

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    credits = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['code']),
        ]
