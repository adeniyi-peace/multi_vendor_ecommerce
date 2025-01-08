from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from django.contrib.auth import login, logout, authenticate

from .forms import  CreateUserForm, UserLoginForm

# Create your views here.


# ~ register users
class RegisterUserView(View):
    def get(self, request):
        form = CreateUserForm()
        context = {"form":form}
        return render(request, "account/register.html", context)
    
    def post(self, request):
        form = CreateUserForm( request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
        
        context = {"form":form}
        return render(request, "account/register.html", context)
    

# ~ login users
class LoginView(View):
    def get(self, request):
        next_redirect = request.GET.get("next", "")
        form = UserLoginForm
        context = {"form":form, "next":next_redirect}
        return render(request, "account/login.html", context)
    
    def post(self, request):
        form = UserLoginForm(request, request.POST)
        next_redirect = request.POST.get("next", "")

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                if next_redirect != "":
                    return redirect(next_redirect)
                return redirect("homepage")

            
        
        context = {"form":form}
        return render(request, "account/login.html", context)
    

# ~ logout users
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("homepage")