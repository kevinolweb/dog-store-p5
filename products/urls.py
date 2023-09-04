from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_products,name="all-products-list"),
    path('<int:product_id>/',views.product_detail_view, name="product-detail"),
]
