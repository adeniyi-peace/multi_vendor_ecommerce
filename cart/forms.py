from django import forms

from dashboard.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ["Shipping_address", "created_by"]