from django.shortcuts import render, redirect
from django.views import View
from projects.models import Project
from review.models import Review
from .forms import ContactForm
from .email import ContactEmail
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from honeypot.decorators import check_honeypot


@method_decorator(check_honeypot, name='dispatch')
class HomepageView(View):

    def featured_reviews(self):
        return Review.objects.filter(featured=True)

    def featured_projects(self):
        return Project.objects.filter(featured=True)

    def get(self, request, *args, **kwargs):
        context = {
            'jobs': self.featured_projects(),
            'form': ContactForm(),
            'reviews': self.featured_reviews(),
        }
        return render(request, 'pages/index.html', context=context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactEmail("email/contact_form_email.html", **form.cleaned_data).send()
            messages.success(request, 'Your message has successfully been sent. I will get back to you soon.', extra_tags='alert-success')
            return redirect('home')
        else:
            messages.error(request, 'Message failed to send. Please make sure to fill out all the form fields.', extra_tags='alert-error')
            return redirect('home')


# 259200 = 30 days
@method_decorator(cache_page(2592000), name='dispatch')
@method_decorator(check_honeypot, name='dispatch')
class HireMeView(View):
    
    def get(self, request):
        form = ContactForm()
        context = { 'form': form }
        return render(request, 'pages/hire_me.html', context=context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactEmail("email/contact_form_email.html", **form.cleaned_data).send()
            messages.success(request, 'Your message has successfully been sent. I will get back to you soon.', extra_tags='alert-success')
            return redirect('home')
        else:
            messages.error(request, 'Message failed to send. Please make sure to fill out all the form fields.', extra_tags='alert-error')
            return redirect('home')
