from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.ver_carrito, name='ver'),
    path('agregar/<int:pk>/', views.agregar, name='agregar'),
    path('eliminar/<int:pk>/', views.eliminar, name='eliminar'),
]