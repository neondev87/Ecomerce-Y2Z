from django.shortcuts import render

def ver_carrito(request):
    return render(request, 'carrito/carrito.html')

def agregar(request, pk):
    return render(request, 'carrito/carrito.html')

def eliminar(request, pk):
    return render(request, 'carrito/carrito.html')