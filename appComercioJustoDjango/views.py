from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import ConsultaForm
from .models import Categoria, Certificacion, Producto


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destacados = []
        for categoria in Categoria.objects.all():
            producto = categoria.productos.order_by('precio').first()
            if producto:
                destacados.append(producto)
        context['destacados'] = destacados
        return context


class PrincipiosView(TemplateView):
    template_name = 'principios.html'


class ProductoListView(ListView):
    queryset = Producto.objects.select_related('categoria')
    template_name = 'productos.html'
    context_object_name = 'productos'


class ProductoBuscarView(View):
    def get(self, request):
        texto = request.GET.get('q', '').strip()
        productos = Producto.objects.select_related('categoria').order_by('nombre')
        if texto:
            productos = productos.filter(nombre__icontains=texto)
        datos = [
            {
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'categoria': producto.categoria.nombre,
                'url': reverse('producto_detalle', args=[producto.id]),
                'url_categoria': reverse('categoria_detalle', args=[producto.categoria.id]),
            }
            for producto in productos
        ]
        return JsonResponse({'productos': datos})


class ProductoDetailView(DetailView):
    queryset = Producto.objects.select_related('categoria').prefetch_related('certificaciones')
    template_name = 'producto_detalle.html'


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias.html'
    context_object_name = 'categorias'


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria_detalle.html'


class CertificacionListView(ListView):
    model = Certificacion
    template_name = 'certificaciones.html'
    context_object_name = 'certificaciones'


class CertificacionDetailView(DetailView):
    queryset = Certificacion.objects.prefetch_related('productos__categoria')
    template_name = 'certificacion_detalle.html'


class ContactoView(CreateView):
    form_class = ConsultaForm
    template_name = 'contacto.html'
    success_url = reverse_lazy('contacto')