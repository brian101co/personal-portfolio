from django.urls import path
from .views import DashboardView, SignupView
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]