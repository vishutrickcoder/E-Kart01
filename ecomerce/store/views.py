from ast import keyword
from itertools import product
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render,get_object_or_404
from carts.models import CartItem
from store.models import Product
from category.models import Category
from carts.utils import _cart_id
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q


def store_home(request,category_slug=None):
    categories = None
    products = None
    products_count = 0


    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category,is_available=True)
    else:
        products = Product.objects.filter(is_available=True)
    
    paginator = Paginator(products,6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    if products:
        products_count = products.count()


    context_data = {
        "products" : paged_products,
        "products_count" : products_count,
    }
    return render(request,"store.html",context_data)


def product_detail(request,category_slug=None,product_slug=None):
    try:
        single_product = Product.objects.get(category__slug=category_slug)
        in_cart = CartItem.objects.filter(cart__cart_id =_cart_id(request),product=single_product).exists()
    except Exception as e:
        print(e)
        raise e
    context_data ={
        "single_product": single_product,
        "in_cart": in_cart,
    }
    return render(request,'product_detail.html',context_data)

def search(request):
    keyword = request.GET.get('keyword')
    products = None
    product_count = 0
    if keyword:
        products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))

        products_count = products.count()
    context = {
        'products' : products,
        'product_count' : product_count,
    }
    return render(request,"store.html",context)

    