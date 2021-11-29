from django.shortcuts import render
from django.views import View
from projects.models import Project

class PortfolioList(View):
    def get(self, request):
        jobs = Project.objects.filter()
        context = {
            'jobs': jobs,
        }
        return render(request, 'pages/portfolio-page.html', context=context)



