from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.db.models import Q
from .models import *
# Create your views here.
def all_products(request):
    products = Product.objects.all()
    query=None
    category=None

    if request.GET:
        if 'category' in request.GET:
            category=request.GET['category']
            products=products.filter(category__name__icontains=category)

    if request.GET:
        if 'q' in request.GET:
            query=request.GET['q']
            if not query:
                messages.error(request,"You never entered a search term!")
                return redirect(reverse,'all-products-list')
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products=products.filter(queries)

    product_list = {
    'products':products,
    'search_term':query,
    'current_categories':category,
    }
    return render(request,'products/all-products.html',product_list)

def product_detail_view(request,product_id):
    product_item=get_object_or_404(Product,pk=product_id)
    context = {
        'product_item':product_item,
    }
    return render(request,'products/product-detail.html',context)