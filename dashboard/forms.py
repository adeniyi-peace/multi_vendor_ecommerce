from django import forms

from .models import Vendor

class RegisterVendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        exclude = ["user"]