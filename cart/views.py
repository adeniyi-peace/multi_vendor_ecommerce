from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

from dashboard.models import Order, OrderItem

from .cart import Cart

# Create your views here.

class CartView(View):
    def get(self, request):
        cart = Cart(request)

        context = {"cart":cart}

        return render(request, "cart/cart.html", context)
    




class AddToCartView(View):
    def get(self, request, id):
        quantity = request.GET.get("quantity","1")
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
    



class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)

        context = {"cart":cart, }

        return render(request, "cart/checkout.html", context)
    


    def post(self, request):
        cart = Cart(request)

        addresses = request.user.address.all()

        if  any("address-option-" in name for name in request.POST.keys()):
            total_price = 0

            """
                implement Payment gateway here using the api
                this might be done later if i get a free paystack or flutterwave
                api key or if i just close eye and register on them
            """

            for things in cart:
                product = things["product"]
                total_price += product.price * int(things["quantity"])
                

            for address in addresses:
                if  request.POST.get(f"address-option-{address.id}"):
                    order=Order.objects.create(first_name=address.first_name, last_name=address.last_name, city=address.city, 
                                        state=address.state, country=address.country, phone_number=address.phone_number, 
                                        paid_amount=total_price,  vendor_id="itouch", created_by=request.user)
                
            for item in cart:
                product = item["product"]
                price = product.price
                quantity =item["quantity"]
                OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            cart.clear()

            return redirect("dashboard")

        context = {"cart":cart}

        return render(request, "cart/checkout.html", context)
