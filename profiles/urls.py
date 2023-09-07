from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('old_orders/<order_number>', views.order_history, name='order_history'),
]
