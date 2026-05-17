from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('historial/', views.historial, name='historial'),
    path('confirmar/', views.confirmar, name='confirmar'),
]