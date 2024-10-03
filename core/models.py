from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.timezone import now


# Create your models here.

# Custom validator for age restriction
def validate_age(value):
    if value < 18 or value > 35:
        raise ValidationError('Age must be between 18 and 35.')

class Registration(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'), 
        ('female', 'Female')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    residence = models.CharField(max_length=50)
    age = models.PositiveIntegerField(validators=[validate_age])  # Age field with restriction
    date_of_birth = models.DateField()  # Date of Birth field
    date_joined = models.DateField()  # Date Joined field
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)  # Gender field with choices
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Attendance(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])
    
    def __str__(self):
        return f"{self.registration.first_name}{self.registration.last_name} - {self.status}"



