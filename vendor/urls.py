from django.urls import path
from . import views

urlpatterns = [
    path("", views.VendorDashboardView.as_view(), name="vendor_dashboard"),

    path("vendor-signup/", views.RegisterVendorView.as_view(), name="vendor_register"),
    path("edit-vendor-profile/", views.EditVendorProfileView.as_view(), name="edit_vendor_profile"),

    path("vendor-order-detail/<int:id>/", views.VendorOrderView.as_view(), name="vendor_order"),

    path("add-product/", views.AddProductView.as_view(), name="add_product"),
    path("edit-product/<slug:slug>/", views.EditProductView.as_view(), name="edit_product"),
    path("delete-product/<slug:slug>/", views.DeleteProductView.as_view(), name="delete_product"),
]
