from django.db import models
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True) 
    join_date = models.DateField(default=timezone.now)
    active = models.BooleanField(default=True)
    #gender = ()


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class AttendanceRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    class Meta:
        unique_together = ('member', 'date')

    def __str__(self):
        return f'{self.member} - {self.date} - {self.status}'