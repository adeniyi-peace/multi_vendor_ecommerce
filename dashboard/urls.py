from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("my-address/", views.UserAddressView.as_view(), name="my_address"),
    path("add-address/", views.AddAddressView.as_view(), name="add_address"),
    path("edit-address/<int:id>", views.EditAddressView.as_view(), name="edit_address"),
    path("delete-address/<int:id>", views.DeleteAddressView.as_view(), name="delete_address"),
]
