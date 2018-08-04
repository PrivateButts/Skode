from django.contrib import admin

from .models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    model = Price
    list_display = ['name', 'print_type', 'print_size', 'price']
