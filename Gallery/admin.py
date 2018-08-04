from django.contrib import admin

from .models import Event, Client, Picture, Gallery


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['pk', 'name', 'date']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['pk', 'name', 'email']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ['pk', 'event', 'client']


admin.site.register(Picture)
