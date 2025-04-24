from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Dashboard view for authenticated users
def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'users/user_dashboard.html')  # Render the user dashboard
    return redirect('login')  # Redirect to login if not authenticated

# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('user_dashboard')  # Redirect to the dashboard
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})  # Render the registration form

# View for displaying the user profile (requires login)
@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})  # Render the profile page

# View for handling user login
def login_view(request):
    if request.method == 'POST':  # Handle POST requests for login
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # Authenticate the user
        if user is not None:
            login(request, user)  # Log the user in
            return render(request, 'login_success.html')  # Show a success page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})  # Show an error message
    return render(request, 'login.html')  # Render the login page for GET requests