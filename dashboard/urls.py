from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),

    path("profile/", views.ProfileView.as_view(), name="user_profile"),
    path("profile/edit-profile/", views.EditProfileView.as_view(), name="edit_profile"),

    path("orders/", views.UserOrderView.as_view(), name="user_order"),

    path("my-address/", views.UserAddressView.as_view(), name="my_address"),
    path("my-address/add-address/", views.AddAddressView.as_view(), name="add_address"),
    path("my-address/edit-address/<int:id>/", views.EditAddressView.as_view(), name="edit_address"),
    path("my-address/delete-address/<int:id>/", views.DeleteAddressView.as_view(), name="delete_address"),

    path("saved-products/", views.SavedProductView.as_view(), name="saved_product"),
    path("saved-products/add-to-saved-item/<int:id>/", views.AddSavedProductView.as_view(), name="add_save"),
    path("saved-products/remove-from-saved-item/<int:id>/", views.RemoveSavedProductView.as_view(), name="remove_save"),
]
