from django.shortcuts import render

def historial(request):
    return render(request, 'pedidos/historial.html')

def confirmar(request):
    return render(request, 'pedidos/confirmar.html')