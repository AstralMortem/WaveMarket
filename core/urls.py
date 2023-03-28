
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('shop.urls')),
    path("account/", include('account.urls')),
    path("cart/", include('cart.urls')),
    path('',include("django.contrib.auth.urls")),
]

