from django.contrib import admin
from django.urls import path, include

# Define the main URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('users/', include('users.urls')),  # Include URLs from the users app
    path('parcels/', include('parcel_app.urls')),  # Include URLs from the parcels app
    path('orders/', include('orders.urls')),  # Include URLs from the orders app
]
