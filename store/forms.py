from django import forms

from dashboard.models import ProductReview

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ["rating", "review"]
        widgets = {"review":forms.Textarea(attrs={"cols":False, "rows":"4", "placeholder":"Write your review..."}),
                   "rating":forms.NumberInput(attrs={"min":"1", "max":"5", "placeholder":"Enter Rating"})}