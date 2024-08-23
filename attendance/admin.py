from django.contrib import admin
from .models import Member, AttendanceRecord

# Register your models here.

admin.site.register(Member)
admin.site.register(AttendanceRecord)