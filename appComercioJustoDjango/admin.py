from django.contrib import admin

from .models import Categoria, Certificacion, Consulta, Producto

admin.site.site_header = 'Comercio Justo · Administración'
admin.site.site_title = 'Comercio Justo'
admin.site.index_title = 'Panel de gestión'


class ProductoInline(admin.TabularInline):
    model = Producto
    fields = ('nombre', 'precio')
    extra = 0
    show_change_link = True


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'num_productos')
    search_fields = ('nombre',)
    inlines = [ProductoInline]

    @admin.display(description='Nº de productos')
    def num_productos(self, obj):
        return obj.productos.count()


@admin.register(Certificacion)
class CertificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio')
    list_editable = ('precio',)
    list_filter = ('categoria', 'certificaciones')
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('certificaciones',)
    list_per_page = 20
    fieldsets = (
        ('Datos del producto', {'fields': ('nombre', 'descripcion', 'precio')}),
        ('Clasificación', {'fields': ('categoria', 'certificaciones')}),
    )


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo_electronico', 'perfil', 'interes')
    list_filter = ('perfil', 'interes')
    search_fields = ('nombre', 'correo_electronico', 'mensaje')
    readonly_fields = ('nombre', 'correo_electronico', 'telefono', 'perfil', 'interes', 'mensaje', 'privacidad')

    def has_add_permission(self, request):
        return False
