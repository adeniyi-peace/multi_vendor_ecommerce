from django.shortcuts import render
from django.http import HttpResponse

from django.views import View

# Create your views here.

def homepage(request):
    return render(request, "store/homepage.html")


class CategoryView(View):
    def get(self, request):
        ...

class listView(View):
    def get(self, request):
        ...


class ProductDetailView(View):
    def get(self, request):
        ...

class CartView(View):
    def get(self, request):
        ...