from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

def view_bag(request):
    #views whats in bag

    return render(request,'bag/bag.html')

def add_to_bag(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag',{})

    if product_id in list(bag.keys()):
        bag[product_id] +=quantity
        messages.info(request, f'Updated the quantity of {product.name} to {bag[product_id]} in your bag!')
    else:
        bag[product_id] = quantity
        messages.success(request, f'Successfully added {product.name} to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_to_bag(request, product_id):
    # Change the quantity of the specified product
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag',{})

    if quantity > 0:
        bag[product_id] = quantity;
        messages.info(request, f'Updated the quantity of {product.name} to {bag[product_id]} in your bag!')
    else:
        bag.pop(product_id)
        messages.success(request, f'Removed a {product.name} from your bag!')

    request.session['bag'] = bag
    return redirect(reverse('bag'))

def remove_from_bag(request, product_id):
    # Remove an item from bag
    try:
        product = get_object_or_404(Product, pk=product_id)
        bag = request.session.get('bag',{})
        bag.pop(product_id)
        request.session['bag'] = bag
        return redirect(reverse('bag'))

    except Exception as e:
        messages.error(request, f'An error occured please try again.')
        return HttpResponse(status=500)

    

    