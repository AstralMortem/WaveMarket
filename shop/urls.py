from django.urls import path, include
from . import views

app_name = "shop"
urlpatterns = [
   path('', views.ItemListView.as_view(), name="item_list"),
   path('product/<slug:slug>/', views.ItemDetailView.as_view(), name="item_detail"),
   path('category/<slug:slug>/', views.CategoryListView.as_view(), name="category_list"),
   path('tags/<slug:slug>/', views.TagsListView.as_view(), name="tags_list"),
   
]

htmx = [
   path('search', views.search, name="search"),
   path('filter', views.filter, name="filter"),
   path('messages', views.messages, name="messages"),
]

urlpatterns += htmx