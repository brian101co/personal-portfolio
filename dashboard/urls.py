from django.urls import path
from .views import DashboardVeiw, UpdateProfileView

urlpatterns = [
    path('profile/update/<int:pk>/', UpdateProfileView.as_view(), name="update-profile"),
    path('', DashboardVeiw.as_view(), name="dashboard"),
]