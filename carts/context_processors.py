from.models import CartItem
from .views import _cart_id

def counter(request):
    
    if('admin' in request.path):
        return {}

    counter = 0

    cart = CartItem.objects.all().filter(cart__cart_id = _cart_id(request))

    for x in cart:
        counter += x.quantity

    return dict(counter = counter)
    
