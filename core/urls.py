from django.urls import path
from .views import (
    index,
    about,
    events,
    contact,
    volunteer,
    connect_group,
    CustomLoginView,
    profile_view,
    attendance_view,
    register_view
)

urlpatterns = [
    path('', index, name='index'),
    #path('index/', views.index, name='index'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('contact/', contact, name='contact'),
    path('volunteer/', volunteer, name='volunteer'),
    path('connect_group/', connect_group, name='connect_group'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile_view, name='profile'),
    path('register/', register_view, name='register'),
    path('attendance/', attendance_view, name='attendance'),
]