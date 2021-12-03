from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

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
        return reverse('project-detail', kwargs={'slug':self.slug})


@receiver(post_save, sender=Project)
def reset_portfolio_list_page_cache(sender, instance, **kwargs):
    if instance.featured:
        featured_key = make_template_fragment_key("featured_projects")
        cache.delete(featured_key)
        return
    portfolio_key = make_template_fragment_key("portfolio_list")
    cache.delete(portfolio_key)
