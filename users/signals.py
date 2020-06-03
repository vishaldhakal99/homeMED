from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import userProfile

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    userProfile.objects.update_or_create(user=instance)