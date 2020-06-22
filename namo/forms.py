from django.contrib.auth.forms import UserCreationForm  # this is django's user creation form
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone', 'note']