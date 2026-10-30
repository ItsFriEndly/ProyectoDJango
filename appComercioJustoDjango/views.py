from django.shortcuts import render, redirect

from .forms import ConsultaForm


def index(request):
    return render(request, 'index.html')


def principios(request):
    return render(request, 'principios.html')


def productos(request):
    return render(request, 'productos.html')


def contacto(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')
    else:
        form = ConsultaForm()
    return render(request, 'contacto.html', {'form': form})
