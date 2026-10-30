from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('principios/', views.principios, name='principios'),
    path('productos/', views.productos, name='productos'),
    path('productos/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<int:pk>/', views.categoria_detalle, name='categoria_detalle'),
    path('certificaciones/', views.certificaciones, name='certificaciones'),
    path('certificaciones/<int:pk>/', views.certificacion_detalle, name='certificacion_detalle'),
    path('contacto/', views.contacto, name='contacto'),
]
