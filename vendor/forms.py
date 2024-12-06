from django import forms

from dashboard.models import Vendor, Product, ProductImage

class RegisterVendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        exclude = ["user"]

# this two class below allows for multiple file uploads in django

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

    # the  get_context function here allows only image files to be uploaded like
    # the image form field. To allow other file type upload remove 
    # def get context or to specify other file uploads change
    # "image/*" to whatever will allow for that specific file type like "video/*" 
    #  furher backend validation is needed to ensure only the specific file needed is uploaded

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["attrs"]["accept"] = "image/*"
        return context

# this class creates a file field that alls multiple file upload, the coded is gotten from
# the django website file uploads. It has been updated by calling functions that allow
# the form to validate if it is empty and flag a 'this field is required error'

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):

        # this validate if the field is empty and raises an error if it is
        self.validate(data)
        self.run_validators(data)

        single_file_clean = super().clean


        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]

        else:
            result = [single_file_clean(data, initial)]

        return result
    
# end of the classes that allows multiple file uploads

class ProductCreationForm(forms.ModelForm):
    Product_pictures = MultipleFileField()
    class Meta:
        model = Product
        exclude = ["user"]

    # this part of this code makes product_picture field not required when the
    # form has been saved once by setting product_picture field to false
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance.id != None:
            self.fields["Product_pictures"].required = False
        

    # second method of saving multiple files to a model that i found of
    # here request is to be called in the function because i make use of request.user object
    # if that is not needed, the request argument can be omitted
    # 
    # if you want to use the first method of saving multiple files to a model check views.py
    # under AddProductView, it has been commented out because i did not use it in this current
    # django project but it works pretty much the same 
    def save(self, request, commit=True):
        product = super().save(commit=False)
        product.user = request.user
        images =self.files.getlist("Product_pictures")

        if commit:
            product.save()
            for image in images:
                ProductImage.objects.create(product=product, image=image)

        return product