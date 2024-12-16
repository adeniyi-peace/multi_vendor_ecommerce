from django.contrib import admin

from .models import Product, Category,ProductImage, Vendor, OrderItem, Order, Address

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"] 
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Vendor)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
