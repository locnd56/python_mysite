from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         """docstring for Meta"""
#         model = CustomUser
#         fields = 'username', 'email', 'date_of_birth'

# class CustomUserChangeForm(UserChangeForm):
#     """docstring for CustomUserChangeForm"""
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'date_of_birth')

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords dont match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'date_of_birth', 'is_active', 'is_superuser')

    def clean_password(self): 
        return self.initial["password"]
