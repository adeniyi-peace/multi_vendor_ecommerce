import os

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings

from django.views import View
from django.views.generic.edit import UpdateView

from .forms import RegisterVendorForm, ProductCreationForm

from dashboard.models import ProductImage, Product

# Create your views here.

class RegisterVendorView(LoginRequiredMixin, View):
    login_url = "/account/login"

    def get(self, request):
        form = RegisterVendorForm()
        context = {"form":form}
        return render(request, "vendor/register_vendor.html", context)
    
    def post(self, request):
        form = RegisterVendorForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            vendor = request.user
            vendor.is_vendor = True
            vendor.save()
            return redirect(reverse("dashboard"))
        
        context = {"form":form}
        return render(request, "vendor/register_vendor.html", context)


class VendorDashboardView(LoginRequiredMixin, View):
    login_url = "/account/login"

    def get(self, request):
        if request.user.is_vendor:
            products = request.user.product.all()
            context ={
                "products":products,
            }
            return render(request, "vendor/vendor_dasbord.html", context)
        
        else:
            return redirect(reverse("dashboard"))
        
class AddProductView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProductCreationForm()
        context ={"form":form}
        return render(request, "vendor/add_product.html", context)
    
    def post(self, request):
        form = ProductCreationForm(request.POST, request.FILES)
        # images = request.FILES.getlist("Product_pictures")

        if form.is_valid():
            form.save(request)
            # form = form.save(commit=False)
            # form.user = request.user
            # product = form.save()
            # 
            # for image in images:
            #     pic = ProductImage(product=form, image=image )
            #     pic.save()
            
            return redirect("vendor_dashboard")

        
        context ={"form":form}
        return render(request, "vendor/add_product.html", context)
    
class EditProductView(LoginRequiredMixin, View):
        
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = ProductCreationForm(instance=product)

        context ={"form":form, "product":product}

        return render(request, "vendor/edit_product.html", context)
    
    def post(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = ProductCreationForm(request.POST, request.FILES, instance=product)
        

        if form.is_valid():
            form.save(request)

            # loops through all instance of images saved for the prduct and puts them in a list
            images = [image for image in product.image.all()]

            for image in images:
                # splits the image name from the image file path i.e product image/white.jpeg return just
                # white.jpeg, it is not needed if i did not split the name in the html file
                folder, name = image.image.name.split("/")

                # the path where the image is stored in the MEDIAL_ROOT
                image_path = image.image.name
                
                # check if one of the checkbox to delete the images has been checked
                if request.POST.get(f"delete-image-{name}"):
                    image.delete()

                    # the rest of the code here deletes the image from the storage folder
                    # this reduces cluter and removes images that won't ever be used
                    file_path = os.path.join(settings.MEDIA_ROOT,  image_path)
                    
                    if os.path.exists(file_path):
                        os.remove(file_path)
                
            
            return redirect("vendor_dashboard")

        
        context ={"form":form, "product":product}
        return render(request, "vendor/edit_product.html", context)
    

class DeleteProductView(LoginRequiredMixin, View):
    def get(self, request, slug):
        if request.user.is_vendor:
            product = get_object_or_404(Product, slug=slug)

            context ={"product":product}
            return render(request, "vendor/delete_product.html", context)
        
    def post(self, request, slug):
        product = get_object_or_404(Product, slug=slug)

        images = [image for image in product.image.all()]

        # removes images from MEDIA_ROOT, again for declutering 
        for image in images:
            image_path = image.image.name
            
            file_path = os.path.join(settings.MEDIA_ROOT,  image_path)
            
            if os.path.exists(file_path):
                os.remove(file_path)
            

        product.delete()
        return redirect("vendor_dashboard")