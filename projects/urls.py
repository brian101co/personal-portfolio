from django.urls import path
from .views import JobListView, JobDetailView, HireMeView, VerifyEmail

app_name = 'projects'

urlpatterns = [
    path('api/verifyemail/<email>', VerifyEmail.as_view(), name='verify-email'),
    path('hire-me/', HireMeView.as_view(), name='hire-me'),
    path('<str:section_id>', JobListView.as_view(), name='project-list-id'),
    path('<str:slug>/', JobDetailView.as_view(), name='project-detail'),
    path('', JobListView.as_view(), name='project-list'),
]