from django.urls import path
from .views import HireMeView, HomepageView

urlpatterns = [
    path('hire-me/', HireMeView.as_view(), name='hire-me'),
    path('<str:section_id>', HomepageView.as_view(), name='project-list-id'),
    path('', HomepageView.as_view(), name='home'),
]