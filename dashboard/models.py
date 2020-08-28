from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    client = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    service = models.ManyToManyField(Service, related_name="projects")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.client}'s Project: {self.title}"

class Update(models.Model):
    update = models.TextField()
    author = models.ForeignKey(User, related_name="updates", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="updates", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.project.title



