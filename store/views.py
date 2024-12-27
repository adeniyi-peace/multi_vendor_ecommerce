from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from django.views import View
from django.views.generic import ListView

from dashboard.models import Product, Category
from .saved_sessions import RecentlyViewed

# Create your views here.

class HomepageView(View):
    def get(self, request):
        model = Product.objects.all()
        categories = Category.objects.all().order_by("?")[:4]
        context ={"products":model, "categories":categories}
        return render(request, "store/homepage.html", context)



class CategoryView(View):
    def get(self, request, category):
        products = Category.objects.get(category=category).product.all()
        context = {"products":products}
        return render(request, "store/list_product.html", context)
    

class ListProductView(ListView):
    model = Product
    template_name = "store/list_product.html"
    context_object_name = "products"



class ProductDetailView(View):
    def get(self, request, slug):
        model = Product.objects.get(slug=slug)
        RecentlyViewed(request).add(str(model.pk))
        context ={"product":model, "slug":model.slug}
        return render(request, "store/product_detail.html", context)
        ...


class SearchView(View):
    def get(self, request):
        search = request.GET.get("q")
        products = Product.objects.filter(Q(Q(name__icontains=search) | Q(description__icontains=search)))
        context = {"products":products}
        return render(request, "store/list_product.html", context)