from django.db import models
from django.utils.text import slugify


from account.models import CustomUser

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField("account.CustomUser", on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to="uploads/profile picture", height_field=None, width_field=None, max_length=None, )
    number = models.CharField(max_length=50)
    is_vendor = models.BooleanField(editable=False, default=False)

class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    city = models.CharField( max_length=100)
    state = models.CharField( max_length=100)
    country = models.CharField( max_length=100)
    phone_number = models.IntegerField()


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    name = models.CharField( max_length=100)
    slug = models.SlugField(unique=True, )
    price = models.IntegerField()
    in_store = models.IntegerField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    ...


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="product image", height_field=None, width_field=None, max_length=None)



class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="review")
    username = models.CharField( max_length=100)
    rating = models.IntegerField()
    review = models.TextField()
