from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('create_new_order/', views.create_new_order),
]