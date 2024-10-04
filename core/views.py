from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm, UserProfileForm
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def events(request):
    return render(request, 'core/events.html')

def contact(request):
    return render(request, 'core/contact.html')

def volunteer(request):
    return render(request, 'core/volunteer.html')

def connect_group (request):
    return render(request, 'core/connect_group.html')

def test (request):
    return render(request, 'core/landing.html')

def home (request):
    return render(request, 'core/home.html')

def profile_success(request):
    # Retrieve the success message from the messages framework
    if messages.get_messages(request):
        return render(request, 'core/profile_success.html')  # Render the success template
    else:
        return redirect('profile_registration')  # Redirect to the registration page if there's no message

def success(request):
    return render(request, 'core/success.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in and redirect to the home page (or any other page)
            auth_login(request, user)
            return redirect('register')  
        else:
            messages.error(request, 'Invalid username or password.!!')

    return render(request, 'core/login.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, "Registration successful! You can now log in.")  # Success message
            return redirect('success')  # Redirect to the login page after signup
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})



@login_required
def register_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Associate the profile with the logged-in user
            user_profile.save()
            
            # Capture the user's first name from the form
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f"Profile registration successful, {first_name}!")
            return redirect('profile_success')  # Redirect to a success page or profile page after registration
    else:
        form = UserProfileForm()

    return render(request, 'core/profile_registration.html', {'form': form})

