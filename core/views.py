from django.shortcuts import render  # noqa
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404  # noqa

from .models import Product, Customer, Order, OrderItem, Address
from .serializers import (
    ProductSerializer,
    CustomerSerializer,
    OrderSerializer,
    OrderItemSerializer,
    AddressSerializer
)
from users.permissions import CanViewAllProducts, CanManageOrders
from django.contrib.auth.decorators import login_required

@login_required
def index_view(request):

    return render(request, 'orders.html')

@login_required
def customer_view(request):
    customer_count = Customer.objects.count()
    return render(request, 'customers.html', {'customer_count':customer_count})

@login_required
def transactions_view(request):
    return render(request, 'transactions.html') 

class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [CanViewAllProducts]


class CustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing customer instances.
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing order instances.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated, CanManageOrders]

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        order = self.get_object()
        items = order.items.all()
        serializer = OrderItemSerializer(items, many=True)
        return Response(serializer.data)


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing order item instances.
    """
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [CanManageOrders]


class AddressViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing address instances.
    """
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated]
