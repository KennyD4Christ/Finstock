"""
URL patterns for the transactions API
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, index_view

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('index/', index_view, name='transactions-index'),  # Add this line
    path('', include(router.urls)),
]
