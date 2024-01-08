from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        subject = 'Welcome to your Module Registration System'
        message = 'Your account and profile has now been created. Please visit the Modules page that is now available to register for select modules!'

        """ send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [sender.email],
            fail_silently=False,
        ) """