from django.urls import path
from .views import JobListView, JobDetailView, HireMeView, DashboardVeiw

app_name = 'jobs'

urlpatterns = [
    path('hire-me/', HireMeView.as_view(), name='hire-me'),
    path('account/dashboard/', DashboardVeiw.as_view(), name='dashboard'),
    path('<str:section_id>', JobListView.as_view(), name='job-list-id'),
    path('<str:slug>/', JobDetailView.as_view(), name='job-detail'),
    path('', JobListView.as_view(), name='job-list'),
]