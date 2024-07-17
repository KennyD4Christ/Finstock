from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Product, Category, ProductImage, Review
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    ProductImageSerializer,
    ReviewSerializer
)

from users.permissions import (
    CanViewAllProducts,
    CanManageOrders,
    CanViewAllTransactions,
    CanManageTransactions,
    CanViewAllInvoices,
    CanManageInvoices
)


from django.shortcuts import render
from .models import Product


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated, CanViewAllProducts]


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated, CanViewAllProducts]

    @action(detail=True, methods=['get'])
    def images(self, request, pk=None):
        product = self.get_object()
        images = product.images.all()
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        product = self.get_object()
        reviews = product.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    @action(
        detail=False,
        methods=['get'],
        permission_classes=[permissions.AllowAny]
    )
    def product_count(self, request):
        """
        Get the product count.
        """
        product_count = Product.objects.count()
        return Response({'product_count': product_count})


class ProductImageViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product image instances.
    """
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
    permission_classes = [permissions.IsAuthenticated, CanViewAllProducts]

    def perform_create(self, serializer):
        product_id = self.request.data.get('product')
        product = get_object_or_404(Product, id=product_id)
        serializer.save(product=product)


class ReviewViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing review instances.
    """
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated, CanViewAllProducts]

    def perform_create(self, serializer):
        product_id = self.request.data.get('product')
        product = get_object_or_404(Product, id=product_id)
        serializer.save(product=product, user=self.request.user)
