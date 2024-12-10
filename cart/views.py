from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View

from .cart import Cart

# Create your views here.

class AddToCartView(View):
    def get(self, request, id):
        quantity = request.GET.get("quantity","")
        cart = Cart(request)
        cart.add(id, quantity=quantity)
        

        return redirect(reverse("homepage"))
    

class UpdateCartView(View):
    def get(self, request, id):
        cart = Cart(request)
        quantity = request.GET.get("quantity")
        cart.add(product_id=id, quantity=quantity, update_quantity=True)

        return redirect(reverse("cart"))
    
class RemoveFromCartView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.remove(id)

        return redirect(reverse("cart"))
    
class CartView(View):
    def get(self, request):
        cart = Cart(request)
        # for car in cart:
        #     print(car)

        context = {"cart":cart}

        return render(request, "cart/cart.html", context)