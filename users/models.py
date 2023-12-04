from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    dob = models.DateField(default = timezone.now)
    street = models.CharField(max_length=100, null = True);
    city = models.CharField(max_length=100, null = True);
    country = models.CharField(max_length=100, null = True);

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
