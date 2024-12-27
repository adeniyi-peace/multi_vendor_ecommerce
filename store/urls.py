from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomepageView.as_view(), name="homepage"),
    path("product/", views.ListProductView.as_view(), name="product"),
    path("category/<str:category>/", views.CategoryView.as_view(), name="list_category"),
    path("product/<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("search/", views.SearchView.as_view(), name="search")
]
