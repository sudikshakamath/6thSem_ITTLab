from django.contrib import admin
from .models import Supplier, InventoryItem

admin.site.register(Supplier)
admin.site.register(InventoryItem)
