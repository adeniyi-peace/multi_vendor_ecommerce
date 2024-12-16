from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

from .forms import AddressForm
from .models import Address



# Create your views here.


class DashboardView(LoginRequiredMixin, View):
    login_url = "/account/login"

    def get(self, request):
        return render(request, "dashboard/account.html")
        ...


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