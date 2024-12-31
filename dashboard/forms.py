from django import forms
from django.contrib.auth.models import User

from .models import Address


class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
        exclude = ["user"]


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={"readonly":True}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={"readonly":True}))

    class Meta:
        model = User
        fields = ["username","email", "first_name", "last_name"]
