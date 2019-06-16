from django.contrib import admin

from .models import CarouselItem


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    model = CarouselItem
    list_display = ['image', 'alt', 'caption', 'button_label', 'button_url']
