from django.urls import path
from . import views

urlpatterns = [
    path('member_list/', views.member_list, name='member_list'),
    path('report/<str:date>/', views.attendance_report, name='attendance_report'),
]
