from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Project


class ProjectListView(View):
    def get(self, request):
        projects = Project.objects.all()
        context = { 'jobs': projects }
        return render(request, 'projects/project_list_page.html', context=context)

class ProjectDetailView(View):
    def get(self, request, slug):
        job = get_object_or_404(Project, slug=slug)
        similar_jobs = Project.objects.exclude(slug=slug)[:3]
        context = {
            'job': job,
            'similar_jobs': similar_jobs,
        }
        return render(request, 'projects/project_detail_page.html', context=context)
        
