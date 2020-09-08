from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django_quill.fields import QuillField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Job(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images/', blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(400, 400)],
                                     format='JPEG',
                                     options={'quality': 95}
    )
    summary = models.TextField()
    body = models.TextField()
    # main_content = QuillField()
    site_url = models.CharField(max_length=150)
    code_url = models.CharField(max_length=150)
    featured = models.BooleanField(default=False)
    testimonial = models.TextField(blank=True)
    reviewer = models.CharField(max_length=120)
    created = models.DateField(blank=True)
    practice = models.BooleanField(default=False)
    
    tags = TaggableManager()

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jobs:job-detail', kwargs={'slug':self.slug})

    def get_portfolio_url():
        return reverse('jobs:job-list-id', kwargs={'section_id': '#portfolio'})

    def get_contact_url():
        return reverse('jobs:job-list-id', kwargs={'section_id': '#contact'})

    def get_about_url():
        return reverse('jobs:job-list-id', kwargs={'section_id': '#whyme'})

       
