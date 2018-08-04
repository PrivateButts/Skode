from django.contrib import admin

from .models import Price, CarouselItem


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    model = Price
    list_display = ['name', 'print_type', 'print_size', 'price']


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    model = CarouselItem
    list_display = ['image', 'alt', 'caption', 'button_label', 'button_url']
