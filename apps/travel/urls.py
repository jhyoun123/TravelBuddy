from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'add_home$', views.add_home),
    url(r'add$', views.add),
    url(r'view/(?P<id>\d+)$', views.view),
    url(r'join/(?P<id>\d+)$', views.join),
]