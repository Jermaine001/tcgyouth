from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    index,
    about,
    events,
    contact,
    volunteer,
    connect_group,
    login,
    test,
    signup,
    home, 
    register_profile, 
    profile_success, 
    success
   
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('contact/', contact, name='contact'),
    path('volunteer/', volunteer, name='volunteer'),
    path('connect_group/', connect_group, name='connect_group'),
    path('login/', login, name='login'), 
    path('signup/', signup, name='signup'),
    path('test/', test, name='test'),
    path('home/', home, name='home'),
    path('register/', register_profile, name='register'),
    path('profile_success/', profile_success, name='profile_success'),
    path('success/', success, name='success')

]