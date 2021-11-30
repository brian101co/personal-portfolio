from django.urls import path
from .views import ProjectDetailView, ProjectListView


urlpatterns = [
    path('<str:slug>/', ProjectDetailView.as_view(), name='project-detail'),
    path('', ProjectListView.as_view(), name='project-list')
]