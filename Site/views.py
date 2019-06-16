from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import CarouselItem, CartItem, Order
from Gallery.models import PricePoint


class Home(TemplateView):
    template_name = "Site/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = CarouselItem.objects.all()
        return context


class About(TemplateView):
    template_name = "Site/about.html"


class Sessions(TemplateView):
    template_name = "Site/sessions.html"


class PriceTable(ListView):
    model = PricePoint
    template_name = "Site/price.html"


class Cart(ListView):
    model = CartItem
    template_name = "Site/cart.html"
