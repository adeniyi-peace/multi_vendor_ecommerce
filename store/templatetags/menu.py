from django import template

from dashboard.models import Category

register = template.Library()

@register.inclusion_tag("menu_items.html")
def menu_items():
    categories = Category.objects.all()
    
    return { "categories":categories }

# this is used in edit.html. did it here cause i did not want to rewrite a template file folder
# it split the image name from the image file path i.e product image/white.jpeg return just
# white .jpeg
@register.filter
def split(value):
    folder, name = value.image.name.split("/")
    return name

