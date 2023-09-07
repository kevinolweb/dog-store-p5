from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import *
from .forms import ProductForm
from django.contrib import messages


def all_products(request):
    products = Product.objects.all()
    query = None
    category = None
    sort = None
    direction = None

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
            category = request.GET['category']
            products = products.filter(category__name__icontains=category)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You never entered a search term!")
                return redirect(reverse, 'all-products-list')
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sort = f'{sort}_{direction}'

    product_list = {
        'products': products,
        'search_term': query,
        'current_categories': category,
        'current_sort': current_sort,
    }
    return render(request,'products/all-products.html',product_list)

def product_detail_view(request, product_id):
    product_item = get_object_or_404(Product, pk=product_id)
    context = {
        'product_item':product_item,
    }
    return render(request,'products/product-detail.html',context)


@login_required
def add_product(request):
    """ Adds product to the store """
    if not request.user.is_superuser:
        messages.error(request,'Sorry only admins can make amends to products!')
        return redirect('all-products-list')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a new product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Oops! Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, prod_id):
    selected_product = get_object_or_404(Product, pk=prod_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=selected_product)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully edited the product.')
            return redirect(reverse('product-detail', args=[selected_product.id]))
        else:
            messages.error(request, 'Oops an error occured editing the product!')
    else:
        form = ProductForm(instance=selected_product)
    context = {
        'form': form,
        'selected_product': selected_product,
    }
    return render(request,'products/edit_product.html', context)

@login_required
def delete_product(request, prod_id):
    selected_product = get_object_or_404(Product, pk=prod_id)
    if request.method == "POST":
        selected_product.delete()
        messages.success(request, 'You have successfully deleted the product.')
        return redirect('all-products-list')
    
    context = {
        'selected_product': selected_product,
    }
    return render(request,'products/delete_product.html', context)
