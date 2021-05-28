from django.shortcuts import render
from django.views import View
from projects.models import Job

class PortfolioList(View):
    def get(self, request):
        jobs = Job.objects.filter(practice=False)
        context = {
            'jobs': jobs,
        }
        return render(request, 'pages/portfolio-page.html', context=context)



