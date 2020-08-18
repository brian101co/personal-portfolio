from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        (None, {
            'fields': ('slug', 'tags')
        }),
        ('Project Details', {
            'fields': ('title', 'image', 'summary', 'body', 'code_url', 'site_url', 'featured')
        }),
        ('Testimonial', {
            'fields': ('testimonial', 'reviewer')
        })
    ]
    list_display = ('title', 'featured')
    list_display_links = ('title', 'featured')
    list_filter = ('featured', 'title')


