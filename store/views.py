from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from dashboard.models import Product

# Create your views here.

class HomepageView(View):
    def get(self, request):
        model = Product.objects.all()
        context ={"products":model}
        return render(request, "store/homepage.html", context)



class CategoryView(View):
    def get(self, request):
        ...

class listView(View):
    def get(self, request):
        ...


class ProductDetailView(View):
    def get(self, request, slug):
        model = Product.objects.get(slug=slug)
        context ={"product":model}
        return render(request, "store/product_detail.html", context)
        ...

class CartView(View):
    def get(self, request):
        ...