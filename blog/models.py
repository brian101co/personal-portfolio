from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_image_thumbnail = ProcessedImageField(
        blank=True,
        upload_to='profile-images/',
        processors=[ResizeToFill(80,80)],
        format='JPEG',
        options={'quality':85}
    )
    display_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.display_name}'s Profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()