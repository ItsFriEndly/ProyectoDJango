import json

from django.conf import settings
from django.core.management.base import BaseCommand

from appComercioJustoDjango.models import Categoria, Certificacion, Producto


class Command(BaseCommand):
    help = 'Exporta categorías, certificaciones y productos a spa/data/datos.json para la SPA de Vue'

    def handle(self, *args, **options):
        datos = {
            'categorias': list(Categoria.objects.order_by('nombre').values('id', 'nombre', 'descripcion')),
            'certificaciones': list(Certificacion.objects.order_by('nombre').values('id', 'nombre', 'descripcion')),
            'productos': [
                {
                    'id': p.id,
                    'nombre': p.nombre,
                    'descripcion': p.descripcion,
                    'precio': float(p.precio),
                    'categoria': p.categoria_id,
                    'certificaciones': [c.id for c in p.certificaciones.all()],
                }
                for p in Producto.objects.order_by('nombre').prefetch_related('certificaciones')
            ],
        }

        ruta = settings.BASE_DIR / 'spa' / 'data' / 'datos.json'
        ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding='utf-8')
        self.stdout.write(self.style.SUCCESS(
            f'{len(datos["productos"])} productos, {len(datos["categorias"])} categorías y '
            f'{len(datos["certificaciones"])} certificaciones exportados a {ruta}'
        ))
