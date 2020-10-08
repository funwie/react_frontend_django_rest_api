from django.urls import path
from order_search.views import OrderList, ItemList, OrderDetail, ItemDetail, api_root

urlpatterns = [
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('', api_root, name='api-root'),
]