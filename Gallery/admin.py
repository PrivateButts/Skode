from django.contrib import admin

from .models import Event, Client, Picture


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['name', 'date']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['name', 'email']


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    model = Picture
    list_display = ['title', 'event', 'client']