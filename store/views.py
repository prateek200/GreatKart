from carts.models import CartItem
from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import category

from carts.views import _cart_id, cart

# Create your views here.

def store(request,category_slug = None):

    products = None 
    categories = None

    if(category_slug != None):
        categories = get_object_or_404(category,slug = category_slug)
        products = Product.objects.all().filter(is_available = True,category = categories)
        products_count = products.count()

    else:
        products = Product.objects.all().filter(is_available = True)
        products_count = products.count()


    context ={
        "products":products,
        "products_count":products_count,
    }

    return render(request,'store/store.html',context)

def product_detail(request,category_slug = None,product_slug = None):
    
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists()
    except Exception as e:
        raise e

    context = {
        "single_product":single_product,
        "in_cart": in_cart,
    }

    return render(request,'store/product_detail.html',context)
    