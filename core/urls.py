from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet,
    CustomerViewSet,
    OrderViewSet,
    OrderItemViewSet,
    AddressViewSet,
)
from .views import index_view, customer_view, transactions_view
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('', index_view, name='orders-index'),
    path('customers/', customer_view, name='customers-index'),
    path('transactions/', transactions_view, name='transactions-index'),
    path('', include(router.urls)),
]
