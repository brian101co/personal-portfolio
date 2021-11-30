from django.shortcuts import render, redirect
from django.views import View
from projects.models import Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.decorators import method_decorator
from .email import ContactEmail

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
        context = {
            'form': form,
        }
        return render(request, 'pages/hire_me.html', context=context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message = f"Hey, my name is { cd['full_name'] }.\n\n { cd['message'] }\n\n My email is { cd['email'] }"
            send_mail(subject, message, 'oliverwebdevelopment2020@gmail.com', ['oliverwebdevelopment2020@gmail.com'])
            messages.success(request, 'Your message has successfully been sent. I will get back to you soon.', extra_tags='alert-success')
            return redirect('home')
        else:
            messages.error(request, 'Message failed to send. Please make sure to fill out all the form fields.', extra_tags='alert-error')
            return redirect('home')
