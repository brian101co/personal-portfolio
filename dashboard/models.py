from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    client = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    service = models.ManyToManyField(Service, related_name="projects")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.client}'s Project: {self.title}"

class Update(models.Model):
    update = models.TextField()
    author = models.ForeignKey(User, related_name="updates", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="updates", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.project.title



