from django.shortcuts import render,redirect

def view_bag(request):
    #views whats in bag

    return render(request,'bag/bag.html')

def add_to_bag(request,product_id):

    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag',{})

    if product_id in list(bag.keys()):
        bag[product_id] +=quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)