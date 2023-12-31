import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product
from django_countries.fields import CountryField
from profiles.models import UserProfile


class Order(models.Model):
    full_name = models.CharField(max_length=55, null=False, blank=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, 
                                    blank=True, null=True, related_name='orders')
    phone_number = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    order_number = models.CharField(max_length=35, null=False, editable=False)
    postal_code = models.CharField(max_length=15, null=True, blank=True)
    town_or_city = models.CharField(max_length=45, null=False, blank=False)
    street_address1 = models.CharField(max_length=70, null=False, blank=False)
    street_address2 = models.CharField(max_length=70, null=True, blank=True)
    county = models.CharField(max_length=40, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generates a random, unique order number for each order
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates grand total each time a line item is added,
        including the delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENT / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the default save method to set the order number
        if not already created.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    num_of_items = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to create lineitem total
        and update the overall order total.
        """
        self.lineitem_total = self.product.price * self.num_of_items
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
