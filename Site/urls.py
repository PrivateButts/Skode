from django.conf.urls import include
from django.urls import path
from django.contrib import admin

from .views import Home, PriceTable, About, Sessions, Cart


app_name = "Site"
urlpatterns = [
    path('', Home.as_view()),
    path('prints/', PriceTable.as_view()),
    path('about/', About.as_view()),
    path('session-info/', Sessions.as_view()),
    path('cart/', Cart.as_view(), name="Cart")
]
