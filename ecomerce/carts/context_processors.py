from carts.models import Cart,CartItem
from carts.utils import _cart_id 

def counter(request):
    cart_count = 0
    cart_items = []
    if 'admin' in request.path:
        return {}
    else:
        cart = Cart.objects.filter(cart_id=_cart_id(request))
        if cart.exists():
            cart_items = CartItem.objects.filter(cart=cart.first())
        for cart_item in cart_items:
            cart_count += cart_item.quantity
    
    return dict(cart_count=cart_count)