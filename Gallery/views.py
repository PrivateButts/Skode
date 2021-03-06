from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView

from .models import Client, Event, Picture, Gallery, PricePoint
from Site.models import CartItem


class EventList(ListView):
    model = Event
    ordering = "-date"


class GalleryByEventList(ListView):
    model = Gallery
    template_name = "Gallery/galleries_by_event_list.html"

    def get_queryset(self, **kwargs):
        return Gallery.objects.filter(event=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Event.objects.get(pk=self.kwargs['id'])
        return context


class GalleryByClientList(ListView):
    model = Gallery
    template_name = "Gallery/galleries_by_client_list.html"

    def get_queryset(self, **kwargs):
        return Gallery.objects.filter(client=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = Client.objects.get(pk=self.kwargs['id'])
        return context


class GalleriesFromEmail(ListView):
    model = Gallery
    template_name = "Gallery/galleries_by_client_list.html"

    def get_queryset(self, **kwargs):
        return Gallery.objects.filter(
            client__email=self.request.GET.get('email', '')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = Client.objects.get(
            email=self.request.GET.get('email', '')
        )
        return context


class PictureByGalleryList(ListView):
    model = Picture
    template_name = "Gallery/pictures_by_gallery_list.html"

    def get_queryset(self, **kwargs):
        return Picture.objects.filter(gallery=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = Gallery.objects.get(pk=self.kwargs['id'])
        return context


class PictureDetails(DetailView):
    model = Picture


def AddPrintsToCart(request):
    prints = request.POST.getlist('PriceOptions')
    pictures = request.POST.getlist('Pictures')

    for picturePK in pictures:
        picture = Picture.objects.get(pk=picturePK)
        for itemPK in prints:
            price = PricePoint.objects.get(pk=itemPK)
            CartItem.objects.create(
                content_object=picture,
                user=request.user,
                price=price.price
            )

    return redirect('Site:Cart')
