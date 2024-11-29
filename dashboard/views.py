from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

from .forms import RegisterVendorForm

# Create your views here.


class DashboardView(LoginRequiredMixin, View):
    login_url = "/account/login"

    def get(self, request):
        return render(request, "dashboard/account.html")
        ...


class RegisterVendorView(LoginRequiredMixin, View):
    login_url = "/account/login"

    def get(self, request):
        form = RegisterVendorForm()
        context = {"form":form}
        return render(request, "dashboard/register_vendor.html", context)
    
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
        return render(request, "dashboard/register_vendor.html", context)


class VendorDashboardView(LoginRequiredMixin, View):
    login_url = "/account/login"

    def get(self, request):
        return render(request, "vendor_dasbord.html")