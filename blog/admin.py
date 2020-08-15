from django.contrib import admin
from .models import Post, Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status',)
    list_filter = ('status', 'created', 'publish', 'author')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Profile)