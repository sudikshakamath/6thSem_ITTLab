from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/', views.inventory_items, name='inventory_items'),
    path('inventory/add/', views.add_inventory_item, name='add_inventory_item'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('suppliers/add/', views.add_supplier, name='add_supplier'),
]
