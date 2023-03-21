from django.urls import path
from . import views
from .views import all_products, product_detail

urlpatterns = [
    path('', all_products, name='products'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('add-to-bag/<item_id>/', views.add_to_bag, name='add_to_bag'),
    
]
