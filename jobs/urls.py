from django.urls import path
from .views import JobListView, JobDetailView

app_name = 'jobs'

urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('<str:slug>/', JobDetailView.as_view(), name='job-detail'),
]