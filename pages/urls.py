from django.urls import path
from .views import PortfolioList

app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioList.as_view(), name='portfolio-list')
]