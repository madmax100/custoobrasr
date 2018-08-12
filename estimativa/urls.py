from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'estimativa'

urlpatterns = [
    url(r'^$', views.home, name='estHome'),
    url(r'^$calculo/', views.calculo, name='calculo')
]