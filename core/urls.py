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
<<<<<<< HEAD
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('connect_group/', views.connect_group, name='connect_group'),
    path('test/', views.test, name='test')

=======
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('contact/', contact, name='contact'),
    path('volunteer/', volunteer, name='volunteer'),
    path('connect_group/', connect_group, name='connect_group'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile_view, name='profile'),
    path('register/', register_view, name='register'),
    path('attendance/', attendance_view, name='attendance'),
>>>>>>> b3708626764c4d592be7f0676534f6e63e145790
]