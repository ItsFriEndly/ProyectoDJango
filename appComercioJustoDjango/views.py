from django.shortcuts import render, redirect, get_object_or_404

from .forms import ConsultaForm
from .models import Producto


def index(request):
    return render(request, 'index.html')


def principios(request):
    return render(request, 'principios.html')


def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})


def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'producto_detalle.html', {'producto': producto})


def contacto(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')
    else:
        form = ConsultaForm()
    return render(request, 'contacto.html', {'form': form})
