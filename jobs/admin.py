from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


