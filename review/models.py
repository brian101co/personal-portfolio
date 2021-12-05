from django.db import models
from projects.models import Project

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key


class Review(models.Model):
    project = models.ForeignKey(
        Project, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="reviews"
    )
    reviewer_photo = models.ImageField(
        upload_to="images/", 
        blank=True
    )
    reviewer_name = models.CharField(max_length=120)
    review_body = models.TextField()
    featured = models.BooleanField(default=False)  

    def __str__(self):
        return self.reviewer_name


@receiver(post_save, sender=Review)
def reset_review_cache(*args, **kwargs):
    featured_key = make_template_fragment_key("featured_reviews")
    cache.delete(featured_key)
