from django.shortcuts import render
from django.views.generic import TemplateView

from .models import CarouselItem, Price


class Home(TemplateView):
    template_name = "Site/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = CarouselItem.objects.all()
        return context
