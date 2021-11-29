from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(
        upload_to='images/', 
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 250)],
        format='JPEG',
        options={'quality': 90}
    )
    summary = models.TextField()
    body = models.TextField()
    site_url = models.URLField(
        max_length=150,
        blank=True, 
        null=True
    )
    code_url = models.URLField(
        max_length=150, 
        blank=True, 
        null=True
    )
    featured = models.BooleanField(default=False)
    testimonial = models.TextField(blank=True)
    reviewer = models.CharField(
        max_length=120, 
        blank=True
    )
    completed_date = models.DateField(blank=True)
    
    tags = TaggableManager()

    class Meta:
        ordering = ('-completed_date',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects:project-detail', kwargs={'slug':self.slug})

       
