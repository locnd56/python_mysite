from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        """docstring for Meta"""
        model = CustomUser
        fields = 'username', 'email', 'date_of_birth'

class CustomUserChangeForm(UserChangeForm):
    """docstring for CustomUserChangeForm"""
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth')

