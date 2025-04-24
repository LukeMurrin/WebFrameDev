from django.shortcuts import render, redirect
from .models import Ad
from .forms import AdForm

# View to list all active ads
def ad_list(request):
    ads = Ad.objects.filter(is_active=True)  # Fetch only active ads
    return render(request, 'ads/ad_list.html', {'ads': ads})

# View to create a new ad
def ad_create(request):
    if request.method == 'POST':  # Handle form submission
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new ad to the database
            return redirect('ad_list')  # Redirect to the ad list page
    else:
        form = AdForm()  # Display an empty form for GET requests
    return render(request, 'ads/ad_form.html', {'form': form})
