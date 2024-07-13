# This file maps URLs to views
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/transactions/', include('transactions.urls')),
    path('api/invoices/', include('invoices.urls')),
    path('api/users/', include('users.urls')),
    path('', include('core.urls')),
    path('', RedirectView.as_view(url='/core/', permanent=False)),  # Redirect root URL to /core/
]
