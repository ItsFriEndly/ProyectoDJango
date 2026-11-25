from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('principios/', views.PrincipiosView.as_view(), name='principios'),
    path('productos/', views.ProductoListView.as_view(), name='productos'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detalle'),
    path('categorias/', views.CategoriaListView.as_view(), name='categorias'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detalle'),
    path('certificaciones/', views.CertificacionListView.as_view(), name='certificaciones'),
    path('certificaciones/<int:pk>/', views.CertificacionDetailView.as_view(), name='certificacion_detalle'),
    path('contacto/', views.ContactoView.as_view(), name='contacto'),
]
