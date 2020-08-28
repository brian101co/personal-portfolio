from django.urls import path
from .views import DashboardVeiw, DashboardMessageAPI, UpdateProfileView

urlpatterns = [
    path('api/messages/', DashboardMessageAPI.as_view()),
    path('api/messages/<user_id>/', DashboardMessageAPI.as_view()), 
    path('profile/update/<int:pk>/', UpdateProfileView.as_view(), name="update-profile"),
    path('', DashboardVeiw.as_view(), name="dashboard"),
]