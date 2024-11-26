from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomepageView.as_view(), name="homepage"),
    path("product/<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail")
]
