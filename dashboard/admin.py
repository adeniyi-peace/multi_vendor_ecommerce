from django.contrib import admin

from .models import Product, Category,ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"] 
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)
