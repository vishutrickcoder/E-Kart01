from unicodedata import category
from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import Category


def store_home(request,category_slug=None):
    categories = None
    products = None
    products_count = 0


    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category,is_available=True)
    else:
        products = Product.objects.filter(is_available=True)
    if products:
        products_count = products.count()


    context_data = {
        "products" : products,
        "products_count" : products_count,
    }
    return render(request,"store.html",context_data)


