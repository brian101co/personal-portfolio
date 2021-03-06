import requests
import json
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Job
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

from django.utils.decorators import method_decorator
from honeypot.decorators import check_honeypot

@method_decorator(check_honeypot, name='dispatch')
class JobListView(View):
    def get_all_jobs(self):
        return Job.objects.all()

    def get_featured_jobs(self):
        return Job.objects.filter(featured=True)

    def get(self, request, *args, **kwargs):
        jobs = self.get_featured_jobs()
        form = ContactForm()
        context = {
            'jobs': jobs,
            'form': form,
        }
        return render(request, 'jobs/jobs_list.html', context=context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message = f"Hey, my name is { cd['full_name'] }.\n\n { cd['message'] }\n\n My email is { cd['email'] }"
            send_mail(subject, message, 'brian@oliverwebdevelopment.com', ['brian@oliverwebdevelopment.com'])
            messages.success(request, 'Your message has successfully been sent. I will get back to you soon.', extra_tags='alert-success')
            return redirect('jobs:job-list')
        else:
            messages.error(request, 'Message failed to send. Please make sure to fill out all the form fields.', extra_tags='alert-error')
            return redirect('jobs:job-list')

class JobDetailView(View):
    def get(self, request, slug):
        job = get_object_or_404(Job, slug=slug)
        similar_jobs = Job.objects.exclude(slug=slug)[:3]
        context = {
            'job': job,
            'similar_jobs': similar_jobs,
        }
        return render(request, 'jobs/jobs_detail.html', context=context)

@method_decorator(check_honeypot, name='dispatch')
class HireMeView(View):
    def get(self, request):
        form = ContactForm()
        context = {
            'form': form,
        }
        return render(request, 'jobs/hire_me.html', context=context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message = f"Hey, my name is { cd['full_name'] }.\n\n { cd['message'] }\n\n My email is { cd['email'] }"
            send_mail(subject, message, 'brian@oliverwebdevelopment.com', ['brian@oliverwebdevelopment.com'])
            messages.success(request, 'Your message has successfully been sent. I will get back to you soon.', extra_tags='alert-success')
            return redirect('jobs:job-list')
        else:
            messages.error(request, 'Message failed to send. Please make sure to fill out all the form fields.', extra_tags='alert-error')
            return redirect('jobs:job-list')

class VerifyEmail(View):
    ''' Verifies and Validates Emails for the SayHello Contact Form '''
    def get(self, request, email):
        url = f'http://apilayer.net/api/check?access_key=6a8ff8af2d3092fa2028a428485af913&email={email}&smtp=1&format=1'
        response = requests.get(url)
        data = json.dumps(response.text)
        return JsonResponse(data, safe=False)
        
