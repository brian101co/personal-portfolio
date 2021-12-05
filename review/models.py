from django.db import models
from projects.models import Project


class Review(models.Model):
    project = models.ForeignKey(
        Project, 
        on_delete=models.SET_NULL, 
        null=True, 
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
