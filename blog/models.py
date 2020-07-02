from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('P', 'Published'),
    ('D', 'Draft'),
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE, 
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES,
                              default='D')
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title