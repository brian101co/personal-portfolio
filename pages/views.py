from django.shortcuts import render, redirect
from django.views import View
from projects.models import Project
from .forms import ContactForm
from .email import ContactEmail
from django.contrib import messages
from django.utils.decorators import method_decorator

from honeypot.decorators import check_honeypot


@method_decorator(check_honeypot, name='dispatch')
class HomepageView(View):
    def get_all_jobs(self):
        return Project.objects.all()

    def get_featured_jobs(self):
        return Project.objects.filter(featured=True)

    def get(self, request, *args, **kwargs):
        jobs = self.get_featured_jobs()
        form = ContactForm()
        context = {
            'jobs': jobs,
            'form': form,
        }
        return render(request, 'pages/index.html', context=context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactEmail.send_email("email/contact_form_email.html", **form.cleaned_data)
            messages.success(request, 'Your message has successfully been sent. I will get back to you soon.', extra_tags='alert-success')
            return redirect('home')
        else:
            messages.error(request, 'Message failed to send. Please make sure to fill out all the form fields.', extra_tags='alert-error')
            return redirect('home')

@method_decorator(check_honeypot, name='dispatch')
class HireMeView(View):
    def get(self, request):
        form = ContactForm()
        context = { 'form': form }
        return render(request, 'pages/hire_me.html', context=context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactEmail.send_email("email/contact_form_email.html", **form.cleaned_data)
            messages.success(request, 'Your message has successfully been sent. I will get back to you soon.', extra_tags='alert-success')
            return redirect('home')
        else:
            messages.error(request, 'Message failed to send. Please make sure to fill out all the form fields.', extra_tags='alert-error')
            return redirect('home')
