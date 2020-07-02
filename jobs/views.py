from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Job

class JobListView(View):
    def get(self, request):
        jobs = Job.objects.all()
        return render(request, 'jobs/jobs_list.html', {'jobs': jobs})

class JobDetailView(View):
    def get(self, request, slug):
        job = get_object_or_404(Job, slug=slug)
        return render(request, 'jobs/jobs_detail.html', {'job': job})

