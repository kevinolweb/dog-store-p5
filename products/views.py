from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def all_products(request):
    products = Product.objects.all()
    product_list = {
    'products':products,
    }
    return render(request,'products/all-products.html',product_list)

def product_detail_view(request,product_id):
    product_item=get_object_or_404(Product,pk=product_id)
    context = {
        'product_item':product_item,
    }
    return render(request,'products/product-detail.html',context)