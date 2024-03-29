from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from modules.models import Module


# Create your models here.

class Registration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    dateOfRegistration = models.DateField(default = timezone.now)

    class Meta:
        unique_together = ('module', 'student')

    def __str__(self):
        return f'{self.student} registered on {self.dateOfRegistration}'
