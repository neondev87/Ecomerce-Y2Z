from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

def catalogo(request):
    productos = Producto.objects.filter(activo=True)
    categorias = Categoria.objects.all()

    categoria_id = request.GET.get('categoria')
    busqueda = request.GET.get('q')

    if categoria_id:
        productos = productos.filter(categoria__id=categoria_id)
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)

    return render(request, 'productos/catalogo.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_id': int(categoria_id) if categoria_id else None,
        'busqueda': busqueda or '',
    })

def detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk, activo=True)
    return render(request, 'productos/detalle.html', {
        'producto': producto,
    })