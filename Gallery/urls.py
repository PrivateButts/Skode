from django.conf.urls import url, include
from django.contrib import admin

from .views import EventList


urlpatterns = [
    url(r'events/$', EventList.as_view()),
]
