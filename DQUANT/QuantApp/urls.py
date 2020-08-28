from django.urls import path
from .import views
import json

urlpatterns = [

    path('',views.sendValue , name = 'sendValue'),
    path('us', views.magazineUS, name = 'magazineUS'),
    path('magazineMain', views.magazineMain, name='magazineMain'),
]