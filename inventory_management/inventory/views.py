from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InventoryItem, Supplier
from .forms import InventoryItemForm, SupplierForm


def home(request):
    return render(request, 'inventory/home.html')


def inventory_items(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/inventory_items.html', {'items': items})


# def add_inventory_item(request):
#     if request.method == 'POST':
#         form = InventoryItem
#     else:
#         form = InventoryItemForm()
#     return render(request, 'inventory/add_inventory_item.html', {'form': form})
def add_inventory_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            print('Form data:', form.cleaned_data)
            return redirect('inventory_items')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/add_inventory_item.html', {'form': form})


def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/suppliers.html', {'suppliers': suppliers})


def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suppliers')
    else:
        form = SupplierForm()
    return render(request, 'inventory/add_supplier.html', {'form': form})
