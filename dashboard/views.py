from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .models import Profile
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.utils import timezone

import json
from django.http import JsonResponse
from django.core import serializers


class DashboardVeiw(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        return render(request, 'dashboard/dashboard.html')

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'dashboard/update_profile.html'
    fields = ('profile_image_thumbnail', 'display_name')
    success_url = reverse_lazy('dashboard')

