from django.contrib import admin
from .forms import StockCreateForm
from .models import Stock

class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name' , 'quantity']
    search_fields = ['category' , 'item_name']
    list_filter = ['category']
    form = StockCreateForm



admin.site.register(Stock, StockCreateAdmin)

# Register your models here.
