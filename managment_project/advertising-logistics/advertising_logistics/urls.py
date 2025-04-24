from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# Define a simple view for the homepage
def homepage(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', homepage, name='homepage'),  # Root URL for the homepage
    path('admin/', admin.site.urls),  # Admin interface
    path('parcels/', include('parcel_app.urls')),  # Parcel app URLs
    path('users/', include('users.urls')),  # Users app URLs
]