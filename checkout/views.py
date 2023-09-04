from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Sorry, your bag is Empty!")
        return redirect(reverse('all-products-list'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Nmgd5JeTK5NfYchZWOc9x98cHNojf6O5J8mlt95fPPtBEwmDjtDvgNvNlokIyipF9HJnXnyyz1MZJqJRmrfHY4q00M1TCOGPv',
        'client_secret': 'test secret',
    }

    return render(request, 'checkout/checkout.html', context)