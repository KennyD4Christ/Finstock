from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockAdjustmentViewSet

router = DefaultRouter()
router.register(r'stock_adjustments', StockAdjustmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
