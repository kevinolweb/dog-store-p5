from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

class Policies(models.Model):
    title=models.CharField(max_length=200)
    info=models.TextField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Policies"

class ProductStatus(models.Model):
    title=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    category=models.ForeignKey('Category',blank=True, null=True, on_delete=models.SET_NULL)
    name=models.CharField(max_length=100)
    sku=models.CharField(max_length=150)
    description=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    policy=models.ForeignKey('Policies',blank=True,null=True, on_delete=models.SET_NULL)
    image_url=models.URLField(max_length=1000,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    on_sale=models.BooleanField(default=False)
    discount_percent=models.CharField(max_length=10,blank=True,null=True)
    in_stock=models.BooleanField(default=True)
    product_status=models.ForeignKey('ProductStatus',blank=True,null=True, on_delete=models.SET_NULL)
    meta_title=models.CharField(max_length=61,blank=True,null=True)
    meta_description=models.CharField(max_length=61,blank=True,null=True)


    def __str__(self):
        return self.name


