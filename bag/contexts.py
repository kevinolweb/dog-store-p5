from decimal import Decimal
from django.conf import settings

def bag_contents(request):
    bag_items=[]
    product_quantity=0
    total=0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENT)
        free_delivery_left = settings.FREE_DELIVERY_THRESHOLD - total
    
    else:
        delivery=0
        free_delviery_left=0

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
