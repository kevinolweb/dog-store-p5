from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_bag,name="bag"),
    path('add/<product_id>',views.add_to_bag,name="add_to_bag"),
]
