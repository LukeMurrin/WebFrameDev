from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL for parcel_app
    path('details/', views.parcel_details, name='parcel_details'),  # New URL for Parcel Details
]