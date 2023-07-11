from django.shortcuts import render
from .models import *
# Create your views here.
def all_products(request):
    products = Product.objects.all()
    product_list = {
    'products':products,
    }
    return render(request,'products/all-products.html',product_list)
