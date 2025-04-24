from django.urls import path
from .views import login_view, profile

# Define URL patterns for the users app
urlpatterns = [
    path('login/', login_view, name='login'),  # URL for the login view
    path('profile/', profile, name='profile'),  # New URL for user profile
]
