from django.contrib import admin

from .models import CarouselItem, CartItem


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    model = CarouselItem
    list_display = ['image', 'alt', 'caption', 'button_label', 'button_url']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ['order', 'item_content_object', 'category_content_object', 'user', 'price', 'taxable', 'tax', 'total', 'status']
