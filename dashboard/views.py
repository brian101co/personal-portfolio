from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from blog.models import Profile
from django.urls import reverse_lazy

from directmessages.apps import Inbox
from directmessages.forms import MessageForm
from django.contrib.auth.models import User
from django.utils import timezone

import json
from django.http import JsonResponse
from django.core import serializers

class DashboardMessageAPI(LoginRequiredMixin, View):
    def get(self, request, user_id, *args, **kwargs):
        ''' 
            Sends back the latest 10 conversation messages between two users.

            Parameters:
            user_id (int): The primary key for user_2

            Returns:
            Lastest 10 Messages between two users as JSON
        '''
        user_1 = User.objects.get(username=request.user.username)
        user_2 = User.objects.get(pk=user_id)
        messages = Inbox.get_conversation(user_1, user_2, 10, True)
        data = serializers.serialize("json", messages)
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        ''' 
            Posts a new message between two users.

            Parameters:
            recipient (int): The primary key for recipient (user)
            content (str): The message

            Returns:
            Lastest 10 Messages between two user as JSON

        '''
        request_data = json.loads(request.body.decode('utf-8'))
        recipient = User.objects.get(pk=request_data['recipient'])
        content = request_data['content']
        sender = User.objects.get(username=request.user.username)

        Inbox.send_message(sender, recipient, content)
        messages = Inbox.get_conversation(sender, recipient, 10, True)
        data = serializers.serialize("json", messages)
        
        return JsonResponse(data, safe=False)
        


class DashboardVeiw(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = MessageForm()
        form.fields['recipient'].queryset = User.objects.filter(username='brianoliver')

        user = User.objects.get(username=request.user.username)
        conversations = Inbox.get_conversations(user)

        context = {
            'form': form,
            'conversations': conversations,
        }
        return render(request, 'dashboard/dashboard.html', context=context)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'dashboard/update_profile.html'
    fields = ('profile_image_thumbnail', 'display_name', 'bio', 'location')
    success_url = reverse_lazy('dashboard')

