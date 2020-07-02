from django.db import models
from django.urls import reverse

class Job(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images/', blank=True)
    summary = models.TextField()
    tech_stack = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jobs:job-detail', kwargs={'slug':self.slug})
