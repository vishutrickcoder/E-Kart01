from itertools import product
from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
# from ecomerce.store.models import variation
from store.models import Product,Variation
from carts.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from carts.utils import _cart_id

# Create your views here.




# adding quantity in a Cart 

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)  # get the product
    product_variation = []
    if request.method =="POST":
        for key, value in request.POST.items():
            try:
                variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                product_variation.append(variation)
            except:
                pass

    try:
        # get the cart using cart id present in session
        cart = Cart.objects.get(cart_id=_cart_id(request))
        
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        
        cart.save()
    
    cart_item_exists = CartItem.objects.filter(product=product , cart=cart).exists()
    
    if cart_item_exists:
        cart_item = CartItem.objects.filter(product=product, cart=cart)

        ex_var_list = []
        var_ids = []

        for item in cart_item:
            existing_variation = item.variations.all().order_by("variation_category")
            ex_var_list.append(list(existing_variation))
            var_ids.append(item.id)

        if product_variation in ex_var_list:
            index = ex_var_list.index(product_variation)
            item_id = var_ids[index]
            item = CartItem.objects.get(product=product , id=item_id)
            item.quantity +=1
            item.save()
        else:
            item =CartItem.objects.get(product=product, quantity=1 , cart=cart)
            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(product_variation)
            item.save()
    else:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        if len(product_variation) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)
        cart_item.save()

   #Save in NOTePAD in courses
    return redirect('ecom-cart')

# This function used for adding item in cart and intially it is 0

def cart(request, total=0 , quantity=0 , cart_item=None):
    TAX_PERCENT = 5
    tax = 0
    grand_total = 0
    cart_items = None
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        # TODO : Add total for each cart item 
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax=(TAX_PERCENT * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax' : tax,
        'grand_total' : grand_total,
    }
    return render(request, 'cart.html',context)

# Remove Items from the Kart 

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('ecom-cart') 

# to Remove Completely Cart Item 

def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product , id=product_id)
    cart_item = CartItem.objects.get(product=product , cart=cart)
    cart_item.delete()
    return redirect('ecom-cart')

