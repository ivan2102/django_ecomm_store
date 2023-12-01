from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('category/<slug:category_slug>/', views.products, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),
    path('search/', views.search, name='search'),
    path('reviews/<int:product_id>/', views.reviews, name='reviews')
]
