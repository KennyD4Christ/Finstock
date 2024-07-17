# users/views.py

from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CustomUser, Role, Permission
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import (
    UserSerializer,
    UserRegistrationSerializer,
    RoleSerializer,
    PermissionSerializer
)
from .permissions import CanViewAllProducts, CanManageOrders  # noqa
from django.shortcuts import render
from core.models import Customer
from products.models import Product

def index_view(request):
    customer_count = Customer.objects.count()
    return render(request, 'customers.html', {'customer_count': customer_count})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to home page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required
def home_view(request):
    product_count = Product.objects.count()
    return render(request, 'orders.html', {'product_count': product_count})

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=False,
        methods=['post'],
        permission_classes=[permissions.AllowAny]
    )
    def register(self, request):
        """
        Register a new user.
        """
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[permissions.AllowAny]
    )
    def customer_count(self, request):
        """
        Get the customer count.
        """
        customer_count = Customer.objects.count()
        return Response({'customer_count': customer_count})

class RoleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing role instances.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermissionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing permission instances.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuthViewSet(viewsets.ViewSet):
    """
    A viewset for user authentication.
    """
    @action(
        detail=False,
        methods=['post'],
        permission_classes=[permissions.AllowAny]
    )
    def login(self, request):
        """
        Log in a user.
        """
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        return Response({'error': 'Invalid Credentials'}, status=400)

    @action(
        detail=False,
        methods=['post'],
        permission_classes=[permissions.IsAuthenticated]
    )
    def logout(self, request):
        """
        Log out a user.
        """
        request.user.auth_token.delete()
        logout(request)
        return Response(status=200)
