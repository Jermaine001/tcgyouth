from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('connect_group/', views.connect_group, name='connect_group'),
    path('test/', views.test, name='test')

]