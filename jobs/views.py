from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Job
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

class JobListView(View):
    def get_all_jobs(self):
        return Job.objects.all()

    def get(self, request, *args, **kwargs):
        jobs = self.get_all_jobs()
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
            send_mail(subject, message, cd['email'], ['oliverwebdevelopment2020@gmail.com'])
            messages.success(request, 'Your message has successfully been sent. I will get back to you soon.', extra_tags='alert-success')
            return redirect('jobs:job-list')
        else:
            messages.error(request, 'Message failed to send. Please make sure to fill out all the form fields.', extra_tags='alert-error')
            return redirect('jobs:job-list')

class JobDetailView(View):
    def get(self, request, slug):
        job = get_object_or_404(Job, slug=slug)
        context = {
            'job': job,
            'urls': {
                'portfolio_url': Job.get_portfolio_url(),
                'contact_url': Job.get_contact_url(),
                'about_url': Job.get_about_url(),
            },
        }
        return render(request, 'jobs/jobs_detail.html', context=context)

class HireMeView(View):
    def get(self, request):
        form = ContactForm()
        context = {
            'form': form,
            'urls': {
                'portfolio_url': Job.get_portfolio_url(),
                'contact_url': Job.get_contact_url(),
                'about_url': Job.get_about_url(),
            },
        }
        return render(request, 'jobs/hire_me.html', context=context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message = f"Hey, my name is { cd['full_name'] }.\n\n { cd['message'] }\n\n My email is { cd['email'] }"
            send_mail(subject, message, cd['email'], ['oliverwebdevelopment2020@gmail.com'])
            messages.success(request, 'Your message has successfully been sent. I will get back to you soon.', extra_tags='alert-success')
            return redirect('jobs:job-list')
        else:
            messages.error(request, 'Message failed to send. Please make sure to fill out all the form fields.', extra_tags='alert-error')
            return redirect('jobs:job-list')
