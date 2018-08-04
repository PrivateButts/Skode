from django.conf.urls import url, include
from django.contrib import admin

from .views import Home, PriceTable


urlpatterns = [
    url(r'^$', Home.as_view()),
    url(r'^prints/$', PriceTable.as_view())
]
