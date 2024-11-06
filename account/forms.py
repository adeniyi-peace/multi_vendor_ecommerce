from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=(TextInput))
    password = forms.CharField(widget=PasswordInput)