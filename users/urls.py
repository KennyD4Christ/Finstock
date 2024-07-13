from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoleViewSet, PermissionViewSet, AuthViewSet, index_view

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('index', index_view, name='customers-index'),  # Add this line
    path('', include(router.urls)),
]

