from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

from .views import EventList, GalleryByEventList, PictureByGalleryList, PictureDetails


urlpatterns = [
    url(r'events/$', EventList.as_view()),
    path('event/<int:id>/', GalleryByEventList.as_view()),
    path('client/<int:id>/', GalleryByEventList.as_view()),

    path('picture/<int:pk>/', PictureDetails.as_view()),

    path('<int:id>/', PictureByGalleryList.as_view()),
]
