from django.contrib import admin

from .models import Event, Client, Picture, Gallery


class PictureInline(admin.StackedInline):
    model = Picture
    extra = 0


class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 0



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['pk', 'name', 'email']
    inlines = [GalleryInline]
    extra = 0


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ['pk', 'event', 'client']
    list_filter = ['event', 'client']
    search_fields = ['pk', 'event__name', 'event__date', 'client__name', 'client__email']
    inlines = [PictureInline]
    extra = 0


admin.site.register(Picture)



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['pk', 'name', 'date']
    inlines = [GalleryInline]
    extra = 0