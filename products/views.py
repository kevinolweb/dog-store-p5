from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.db.models import Q
from django.db.models.functions import Lower
from .models import *
# Create your views here.
def all_products(request):
    products = Product.objects.all()
    query=None
    category=None
    sort=None
    direction=None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

    current_sort =f'{sort}_{direction}'

    product_list = {
    'products':products,
    'search_term':query,
    'current_categories':category,
    'current_sort':current_sort,
    }
    return render(request,'products/all-products.html',product_list)

def product_detail_view(request,product_id):
    product_item=get_object_or_404(Product,pk=product_id)
    context = {
        'product_item':product_item,
    }
    return render(request,'products/product-detail.html',context)