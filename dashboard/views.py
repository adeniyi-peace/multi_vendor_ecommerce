from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

from .forms import AddressForm
from .models import Address, Product, Order
from store.saved_sessions import SavedProduct
from .forms import UpdateUserForm



# Create your views here.


class DashboardView(LoginRequiredMixin, View):
    login_url = "/account/login"

    def get(self, request):
        return render(request, "dashboard/account.html")
        


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        context = {"user":request.user}
        return render(request, "dashboard/profile.html", context)


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UpdateUserForm(instance=request.user)
        context = {"form":form}
        return render(request, "dashboard/edit_profile.html", context)
    
    def post(self, request):
        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse("user_profile"))
        
        context = {"form":form}
        return render(request, "dashboard/edit_profile.html", context)



class UserOrderView(LoginRequiredMixin, View):
    def get(self, request):
        orders = request.user.order.all()
        context = {"orders":orders}
        print(orders)
        return render(request, "dashboard/orders.html", context)





class UserAddressView(LoginRequiredMixin, View):
    def get(self, request):

        return render(request, "dashboard/my_address.html")
    

class AddAddressView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddressForm()

        previous_page=""
        # This code ensures gets the previous page url and inputs it in the template as an hidden input
        if request.META.get("HTTP_REFERER") != request.build_absolute_uri() :

            # the essence of ensuring the page is redirected to the previous page is because of the checkout view
            # hence i decide to hard encode it here so that if i go to add/edit address from another view it will do the 
            # normal redirect 
            if request.META.get("HTTP_REFERER")!= None and "checkout" in request.META.get("HTTP_REFERER"):

                previous_page = request.META.get("HTTP_REFERER")

        context = {"form":form, "next":previous_page} 
        return render(request, "dashboard/add_address.html", context)
    

    def post(self, request):
        form = AddressForm(request.POST)

        # We get the value of the previous post stored in the hidden input with the name next
        previous_page = request.POST.get("next")

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            # confirms if the next is not empty and redirects to the previous page
            # problem is that this works even when i get to the page through an unauthorized url
            # will try fixing the problem from the if statement in the get
            #  note to self: i have patched the problem with an if statement
            if previous_page != "":
                return redirect(previous_page)

            return redirect("my_address")
        
        context = {"form":form} 
        return render(request, "dashboard/add_address.html", context)



class EditAddressView(LoginRequiredMixin, View):
    def get(self, request, id):
        address = get_object_or_404(Address, id=id)
        form = AddressForm(instance=address)

        previous_page=""

        if request.META.get("HTTP_REFERER") != request.build_absolute_uri() :

            if request.META.get("HTTP_REFERER")!= None and "checkout" in request.META.get("HTTP_REFERER"):

                previous_page = request.META.get("HTTP_REFERER")

        context = {"form":form, "next":previous_page} 
        return render(request, "dashboard/edit_address.html", context)
    
    def post(self, request, id):
        address = get_object_or_404(Address, id=id)
        form = AddressForm(request.POST, instance=address)

        previous_page = request.POST.get("next")


        if form.is_valid():
            form.save()

            if previous_page != "":
                return redirect(previous_page)

            return redirect("my_address")
        
        context = {"form":form} 
        return render(request, "dashboard/edit_address.html", context)
    

class DeleteAddressView(LoginRequiredMixin, View):
    def get(self, request, id):
        address = get_object_or_404(Address, id=id)
        address.delete()
        return redirect(reverse("my_address"))


class SavedProductView(View):
    def get(self, request):
        saved = SavedProduct(request)

        # to future peace, i decided to call the objects from here and not inside from the SavedProduct
        # class because i might use pagination, calling it here allows for easier pagination logic
        saved_products = Product.objects.filter(id__in=saved.items())


        context = {"saved_products":saved_products}
        return render(request, "dashboard/saved_product.html", context)

class AddSavedProductView(View):
    def get(self, request, id):
        saved_product = SavedProduct(request)
        saved_product.add(id)
        return redirect(request.META.get("HTTP_REFERER", "/"))
    

class RemoveSavedProductView(View):
    def get(self, request, id):
        saved_product = SavedProduct(request)
        saved_product.delete(id)
        return redirect(request.META.get("HTTP_REFERER", "/"))