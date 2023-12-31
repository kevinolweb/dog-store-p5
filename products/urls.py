from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="all-products-list"),
    path('<int:product_id>/', views.product_detail_view, name="product-detail"),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:prod_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:prod_id>/', views.delete_product, name='delete_product'),
]
