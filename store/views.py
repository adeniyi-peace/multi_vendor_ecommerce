from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q

from django.views import View
from django.views.generic import ListView

from dashboard.models import Product, Category, Vendor
from .saved_sessions import RecentlyViewed, SavedProduct
from .forms import ProductReviewForm

# Create your views here.

class HomepageView(View):
    def get(self, request):
        model = Product.objects.all()
        categories = Category.objects.all().order_by("?")[:4]
        vendors = Vendor.objects.all().order_by("?")[:3]
        saved = SavedProduct(request)
        context ={"products":model, "categories":categories, "saved":saved, "vendors":vendors}
        return render(request, "store/homepage.html", context)



class CategoryView(View):
    def get(self, request, category):
        products = Category.objects.get(category=category).product.all()
        saved = SavedProduct(request)
        context = {"products":products, "saved":saved}
        return render(request, "store/list_product.html", context)
    

class ListProductView(ListView):
    model = Product
    template_name = "store/list_product.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        saved = SavedProduct(self.request)
        context["saved"] = saved
        return context




class ProductDetailView(View):
    def get(self, request, slug):
        model = Product.objects.get(slug=slug)

        RecentlyViewed(request).add(str(model.pk))

        saved = SavedProduct(request)

        form = ProductReviewForm()
        

        context ={"product":model, "slug":model.slug, "saved":saved, "form":form}

        return render(request, "store/product_detail.html", context)
    

    def post(self, request, slug):
        model = Product.objects.get(slug=slug)

        saved = SavedProduct(request)

        form = ProductReviewForm(request.POST)

        if form.is_valid():
            if request.user.username!="":
                form = form.save(commit=False)
                form.product = model
                form.username = request.user.username
                form.save()
                return redirect(reverse("product_detail", args=[slug]))
            
            else:
                messages.info(request, "Login to Submit Review")
            
        else:
            messages.info(request, "Error in submitting Review")

        context ={"product":model, "slug":model.slug, "saved":saved, "form":form}

        return render(request, "store/product_detail.html", context)




class SearchView(View):
    def get(self, request):
        search = request.GET.get("q")
        products = Product.objects.filter(Q(Q(name__icontains=search) | Q(description__icontains=search)))
        context = {"products":products}
        return render(request, "store/list_product.html", context)