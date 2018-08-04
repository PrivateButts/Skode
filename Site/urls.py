from django.conf.urls import url, include
from django.contrib import admin

from .views import Home


urlpatterns = [
    url(r'^$', Home.as_view()),
]
