# myapp/backends.py
from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend

class EmailOrUsernameBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the username is an email
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                # Fallback to checking username
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
