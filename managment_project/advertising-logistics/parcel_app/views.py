from django.http import HttpResponse

# View for the Parcel App homepage
def index(request):
    return HttpResponse("Welcome to the Parcel App!")  # Display a welcome message

# View for displaying parcel details
def parcel_details(request):
    return HttpResponse("This is the Parcel Details page!")  # Display parcel details