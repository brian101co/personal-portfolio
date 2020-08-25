from django.shortcuts import render
from django.views import View
from jobs.models import Job

class PortfolioList(View):
    def get(self, request):
        jobs = Job.objects.all()
        context = {
            'jobs': jobs,
             'urls': {
                'portfolio_url': Job.get_portfolio_url(),
                'contact_url': Job.get_contact_url(),
                'about_url': Job.get_about_url(),
            },
        }
        return render(request, 'pages/portfolio-page.html', context=context)



