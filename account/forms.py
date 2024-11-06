from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm

from .models import CustomUser

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=(TextInput))
    password = forms.CharField(widget=PasswordInput)