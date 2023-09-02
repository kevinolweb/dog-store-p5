from django.shortcuts import render, redirect, reverse

def view_bag(request):
    #views whats in bag

    return render(request,'bag/bag.html')

def add_to_bag(request, product_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag',{})

    if product_id in list(bag.keys()):
        bag[product_id] +=quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_to_bag(request, product_id):
    # Change the quantity of the specified product
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag',{})

    if quantity > 0:
        bag[product_id] = quantity;
    else:
        bag.pop(product_id)

    request.session['bag'] = bag
    return redirect(reverse('bag'))

def remove_from_bag(request, product_id):
    # Change the quantity of the specified product
    bag = request.session.get('bag',{})
    bag.pop(product_id)

    request.session['bag'] = bag
    return redirect(reverse('bag'))