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
    image = models.ImageField(upload_to="uploads/product image", height_field=None, width_field=None, max_length=None)
    price = models.IntegerField()
    in_store = models.IntegerField()
    description = models.TextField()
    ...

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="review")
    username = models.CharField( max_length=100)
    rating = models.IntegerField()
    review = models.TextField()

