from django.shortcuts import get_object_or_404, redirect, render

from .forms import ConsultaForm
from .models import Categoria, Certificacion, Producto


def index(request):
    destacados = []
    for categoria in Categoria.objects.all():
        producto = categoria.productos.order_by('precio').first()
        if producto:
            destacados.append(producto)
    return render(request, 'index.html', {'destacados': destacados})


def principios(request):
    return render(request, 'principios.html')


def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})


def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto_detalle.html', {'producto': producto})


def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})


def categoria_detalle(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'categoria_detalle.html', {'categoria': categoria})


def certificaciones(request):
    certificaciones = Certificacion.objects.all()
    return render(request, 'certificaciones.html', {'certificaciones': certificaciones})


def certificacion_detalle(request, pk):
    certificacion = get_object_or_404(Certificacion, pk=pk)
    return render(request, 'certificacion_detalle.html', {'certificacion': certificacion})


def contacto(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')
    else:
        form = ConsultaForm()
    return render(request, 'contacto.html', {'form': form})