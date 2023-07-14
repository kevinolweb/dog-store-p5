from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items=[]
    product_quantity=0
    total=0

    bag = request.session.get('bag',{})
    
    for product_id, quantity in bag.items():
        product = get_object_or_404(Product,pk=product_id)
        total += product.price
        product_quantity = quantity
        bag_items.append({
            'product_id':product_id,
            'quantity':quantity,
            'product':product,
        }
        )


    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENT)
        free_delivery_left = settings.FREE_DELIVERY_THRESHOLD - total
    
    else:
        delivery=0 
        free_delivery_left=0

    grand_total = total + delivery

    context = {
        'bag_items':bag_items,
        'grand_total':grand_total,
        'product_quantity':product_quantity,
        'delivery':delivery,
        'free_delivery_left':free_delivery_left,
        'free_delivery_threshold':settings.FREE_DELIVERY_THRESHOLD,
    }
    return context
