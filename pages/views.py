from django.shortcuts import render
from django.views.generic import ListView
from jobs.models import Job

class PortfolioListView(ListView):
    template_name = 'pages/portfolio-page.html'
    model = Job
