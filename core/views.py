from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
from django.contrib import messages



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


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in and redirect to the home page (or any other page)
            auth_login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.!!')

    return render(request, 'core/login.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, "Registration successful.")
            return render(request, 'core/success.html')  # Render the success template
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form': form})
