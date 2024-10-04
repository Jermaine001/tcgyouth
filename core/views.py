from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Registration, Attendance
from django.contrib.admin.views.decorators import staff_member_required



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
<<<<<<< HEAD
=======
<<<<<<< HEAD

def test (request):
    return render (request, 'core/landing.html')
=======
#login view user the django authenication
#class CustomLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'core/login.html', {'form': form})
>>>>>>> origin/main

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Log in the user
                return redirect('home')  # Redirect to a home page or wherever you want
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
<<<<<<< HEAD
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})
=======
        form = RegistrationForm()

    return render(request, 'core/registration.html', {'form': form})
    
#Attendance View
@staff_member_required
def attendance_view(request):
    registrations = Registration.objects.all()
    
    if request.method == 'POST':
        for registration in registrations:
            status = request.POST.get(f'attendance_{registration.id}')
            Attendance.objects.create(registration=registration, status=status)
        return redirect('attendance_success')  # Redirect to a success page after marking attendance

    return render(request, 'core/attendance.html', {'registrations': registrations})
>>>>>>> b3708626764c4d592be7f0676534f6e63e145790
>>>>>>> origin/main
