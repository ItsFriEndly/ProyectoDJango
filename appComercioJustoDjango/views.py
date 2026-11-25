from django.urls import reverse_lazy
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
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'


class ProductoDetailView(DetailView):
    model = Producto
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
    model = Certificacion
    template_name = 'certificacion_detalle.html'


class ContactoView(CreateView):
    form_class = ConsultaForm
    template_name = 'contacto.html'
    success_url = reverse_lazy('contacto')