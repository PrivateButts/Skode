from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Client, Event, Picture


class EventList(ListView):
    model = Event

