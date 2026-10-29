from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def principios(request):
    return render(request, 'principios.html')


def productos(request):
    return render(request, 'productos.html')


def contacto(request):
    return render(request, 'contacto.html')
