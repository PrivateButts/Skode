from django.conf.urls import url, include
from django.contrib import admin

from .views import Home, PriceTable, About, Sessions


urlpatterns = [
    url(r'^$', Home.as_view()),
    url(r'^prints/$', PriceTable.as_view()),
    url(r'^about/$', About.as_view()),
    url(r'^session-info/$', Sessions.as_view())
]
