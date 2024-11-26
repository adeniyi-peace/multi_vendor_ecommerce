from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("sign-up/", views.RegisterUserView.as_view(), name="register"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
