from django.db import models
from django.contrib.auth.models import Group

# Create your models here.

class CourseGroup(Group):
    description = models.TextField(blank=True)
