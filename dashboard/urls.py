from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("vendor-signup/", views.RegisterVendorView.as_view(), name="vendor_register")
]
