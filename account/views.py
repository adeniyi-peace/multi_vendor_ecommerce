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
        return HttpResponse("signup")
    
    def post(self, request):
        form = CreateUserForm(request, request.POST)

        if form.is_valid():
            form.save()
            # return redirect("login")
        
        context = {"form":form}
        return HttpResponse("signup")
    

# ~ login users
class LoginView(View):
    def get(self, request):
        form = UserLoginForm
        context = {"form":form}
        return HttpResponse("login")
    
    def post(self, request):
        form = UserLoginForm(request, request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                # return redirect("homepage")

            
        
        context = {"form":form}
        return HttpResponse("signup")
    

# ~ logout users
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("homepage")