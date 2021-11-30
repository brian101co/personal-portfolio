from django.contrib import admin
from .models import Service, Project, Update, Profile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
