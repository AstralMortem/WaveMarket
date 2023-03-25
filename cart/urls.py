
from . import views
from django.urls import path, include

app_name = "cart"
urlpatterns = [
    path("", views.cart_view, name="cart"),
    path("add/<int:items_id>", views.cart_add, name="cart-add"),
    path("remove/<int:items_id>", views.cart_remove, name="cart-remove"),
    path("length", views.cart_length, name="cart-length"),
    path('coupon/add/', views.coupon_add, name="coupon-add"),
    path('coupon/remove/', views.coupon_remove, name="coupon-remove"),
    path('payment', views.payment_view, name="payment"),
    path('payment-finish/', views.payment_finish, name="payment-finish"),
    path('payment-service/', views.payment_service, name="payment-service"),
    path('order-delete/<uuid:id>', views.delete_order, name="order-delete")
]
