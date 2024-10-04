# core/forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
