from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'The was profile was updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {
        'form': form,
        'orders': orders,
        'profile_page_true': True,
    }

    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a previous confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
