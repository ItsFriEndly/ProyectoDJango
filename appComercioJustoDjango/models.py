
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Certificacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="productos"
    )

    certificaciones = models.ManyToManyField(
        Certificacion,
        blank=True,
        related_name="productos"
    )

    def __str__(self):
        return self.nombre


class Consulta(models.Model):

    PERFIL_CHOICES = [
        ('consumidor', 'Consumidor'),
        ('productor', 'Productor'),
    ]

    INTERES_CHOICES = [
        ('cafe', 'Café'),
        ('cacao', 'Cacao'),
        ('te', 'Té'),
        ('azucar', 'Azúcar de caña'),
    ]

    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=10, validators=[
        MinLengthValidator(9, message='El teléfono debe tener al menos 9 dígitos.'),
        MaxLengthValidator(10, message='El teléfono no puede tener más de 10 dígitos.'),
        RegexValidator(regex=r'^\d+$', message='El teléfono debe contener únicamente números.')])
    privacidad = models.BooleanField(default=False)
    mensaje = models.TextField(blank=True, null=True)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES, default='consumidor')
    interes = models.CharField(max_length=20, choices=INTERES_CHOICES, default='cafe')

    def __str__(self):
        return f"Consulta de {self.nombre} ({self.correo_electronico})"