from django.shortcuts import render, redirect

# Create your views here.
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