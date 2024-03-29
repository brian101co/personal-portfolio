from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .models import Profile
from django.urls import reverse_lazy

from django.contrib.auth.models import User


class DashboardVeiw(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        return render(request, 'dashboard/dashboard.html')

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'dashboard/update_profile.html'
    fields = ('profile_image_thumbnail', 'display_name', 'email')
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user.id == request.user.id:
            return super().get(request, *args, **kwargs)
        return redirect('dashboard')

