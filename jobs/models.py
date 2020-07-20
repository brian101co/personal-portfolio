from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

class Job(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images/', blank=True)
    summary = models.TextField()
    body = models.TextField()
    site_url = models.CharField(max_length=150)
    code_url = models.CharField(max_length=150)

    tags = TaggableManager()
    
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

       
