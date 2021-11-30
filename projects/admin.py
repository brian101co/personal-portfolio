from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        (None, {
            'fields': ('slug', 'tags', 'completed_date')
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


