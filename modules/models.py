from django.db import models
from django.contrib.auth.models import Group
#from course.models import Course


# Create your models here.

class Module(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    credit = models.CharField(max_length=3)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    availability = models.BooleanField()
    course = models.ManyToManyField(Group, related_name = 'modules')

    def __str__(self):
        return self.name


# course = Course.objects.get(pk=1)
# new_module = Module()
# new_module.name = "Designing Cloud Based Systems"
# new_module.course = course
# new_module.save()

# course = Course.objects.get(pk=1)
# new_module = Module()
# new_module.name = "Advanced Data Management"
# new_module.course = course
# new_module.save()

