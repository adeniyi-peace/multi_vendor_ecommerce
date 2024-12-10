from django.urls import path
from . import views

urlpatterns = [
    path("", views.CartView.as_view(), name="cart"),
    path("add-to-cart/<int:id>/", views.AddToCartView.as_view(), name="add_to_cart"),
    path("update-cart/<int:id>/", views.UpdateCartView.as_view(), name="update_cart"),
    path("remove_from_cart/<str:id>/", views.RemoveFromCartView.as_view(), name="remove_from_cart")
]
