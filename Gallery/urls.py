from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

from . import views

app_name = 'Gallery'
urlpatterns = [
    url(r'events/$', views.EventList.as_view()),
    path('event/<int:id>/', views.GalleryByEventList.as_view()),
    path('client/<int:id>/', views.GalleryByClientList.as_view()),
    path('email/', views.GalleriesFromEmail.as_view()),

    path('picture/<int:pk>/', views.PictureDetails.as_view()),
    path('pictures/cart/', views.AddPrintsToCart, name='AddPrintsToCart'),

    path('<int:id>/', views.PictureByGalleryList.as_view()),
]
