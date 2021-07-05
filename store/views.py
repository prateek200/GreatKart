from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import category

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
