from django.urls import path
from . import views

# URL patterns for the ads app
urlpatterns = [
    path('', views.ad_list, name='ad_list'), # List all ads
    path('create/', views.ad_create, name='ad_create'), # Create a new ad
]
