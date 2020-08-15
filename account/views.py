from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from .forms import SignupForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name="get")
class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'account/dashboard.html')

class SignupView(View):
    def get(self, request, *args, **kwargs):
        user_form = SignupForm()
        return render(request, 'account/signup.html', {'user_form':user_form})

    def post(self, request, *args, **kwargs):
        user_form = SignupForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/signup_complete.html', {'new_user':new_user})
        else:
            user_form = SignupForm()
            return render(request, 'account/signup.html', {'user_form':user_form})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'account/login.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    
           
                    