from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'price',
        'image',
        'in_stock'
    )
    ordering = ('name',)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Policies)
admin.site.register(ProductStatus)