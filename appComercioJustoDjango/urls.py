from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('principios/', views.principios, name='principios'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/<int:id>/', views.producto_detalle, name='producto_detalle'),
]
