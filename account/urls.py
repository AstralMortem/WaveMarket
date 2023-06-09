from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views    
from . import views


app_name = 'account'

urlpatterns = [
   path('signup/', views.UserRegisterView.as_view(), name="signup"),
   path('', views.profile_view, name="profile"),
   path('orders/', views.order_view, name="orders"),

]

htmx = [
   path('address/add', views.add_address, name="address-add"),
   path('address/<int:id>', views.update_address, name="address-update"),
   path('address/<int:id>/delete', views.delete_address, name="address-delete"),
   path('update/', views.user_setup_update, name="profile-update")
]

urlpatterns += htmx