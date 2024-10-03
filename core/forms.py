# myapp/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Registration

#login Form 
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email', max_length=254)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            # You can add additional validation here if needed
            pass
        return self.cleaned_data
    

#Registration  For Form TCG 
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'residence', 'age', 'gender', 'date_of_birth']

