from django.db import models

from account.models import CustomUser

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField("account.CustomUser", on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to="uploads/profile picture", height_field=None, width_field=None, max_length=None)
    number = models.CharField(max_length=50)

class Category(models.Model):
    category = models.CharField(max_length=50)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    name = models.CharField( max_length=100)
    slug = models.SlugField()
    price = models.IntegerField()
    in_store = models.IntegerField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)
    ...


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="product image", height_field=None, width_field=None, max_length=None)



class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="review")
    username = models.CharField( max_length=100)
    rating = models.IntegerField()
    review = models.TextField()
