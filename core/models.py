from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import date


# Create your models here.

# Custom validator for age restriction

def validate_age(value):
    # Check if the age is between 18 and 35
    if value < 18 or value > 35:
        raise ValidationError('Age must be between 18 and 35.')
class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
    ]

    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField(editable=False) 
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    residence = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically calculate age based on date_of_birth
        if self.date_of_birth:
            today = date.today()
            self.age = today.year - self.date_of_birth.year - \
                       ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"





