from django.shortcuts import render, redirect
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login as auth_login
#from django.views import View
#from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import RegistrationForm
from django.contrib.auth import login as auth_login
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

def test (request):
    return render (request, 'core/landing.html')
=======
#login view user the django authenication
#class CustomLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'core/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
        return render(request, 'core/login.html', {'form': form})

#profile redirection html after authentification
def profile_view(request):
    return render(request, 'core/profile.html')


# Login View


class CustomLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'core/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
        return render(request, 'core/login.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'core/profile.html')


#Registration Views


@login_required
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.save()
            return redirect('profile')  # Redirect to a success page
    else:
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
