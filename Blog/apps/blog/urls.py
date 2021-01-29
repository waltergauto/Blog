from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name = 'index'),
    path('generales/', generales, name = 'generales'),
    path('redes/', redes, name = 'redes'),
    path('videojuegos/', videojuegos, name = 'videojuegos'),
    path('programacion/', programacion, name = 'programacion'),
    path('<slug:slug>/', detallePost, name = 'detalle_post')
]