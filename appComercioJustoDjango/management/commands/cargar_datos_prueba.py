
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from appComercioJustoDjango.models import (
    Categoria,
    Certificacion,
    Producto,
)


class Command(BaseCommand):
    help = "Crea datos de prueba para Comercio Justo"

    @transaction.atomic
    def handle(self, *args, **options):
        # 1. Crear categorías
        categorias_data = [
            {
                "nombre": "Alimentacion",
                "descripcion": (
                    "Productos alimentarios de comercio justo "
                    "y consumo responsable."
                ),
            },
            {
                "nombre": "Cafe e infusiones",
                "descripcion": (
                    "Cafes, tes e infusiones procedentes "
                    "de productores responsables."
                ),
            },
            {
                "nombre": "Chocolate y dulces",
                "descripcion": (
                    "Chocolates y dulces elaborados con "
                    "ingredientes de origen responsable."
                ),
            },
            {
                "nombre": "Ropa y complementos",
                "descripcion": (
                    "Prendas y complementos fabricados "
                    "con criterios eticos."
                ),
            },
            {
                "nombre": "Hogar",
                "descripcion": (
                    "Articulos para el hogar producidos "
                    "de forma responsable."
                ),
            },
            {
                "nombre": "Cosmetica natural",
                "descripcion": (
                    "Productos de cuidado personal "
                    "con ingredientes de origen natural."
                ),
            },
        ]

        categorias = {}

        for datos in categorias_data:
            categoria, creada = Categoria.objects.get_or_create(
                nombre=datos["nombre"],
                defaults={"descripcion": datos["descripcion"]},
            )
            categorias[categoria.nombre] = categoria

        # 2. Crear certificaciones
        certificaciones_data = [
            {
                "nombre": "Fairtrade",
                "descripcion": (
                    "Certificacion de comercio justo "
                    "para productos y cadenas de suministro "
                    "que cumplen sus criterios."
                ),
            },
            {
                "nombre": "Ecologico UE",
                "descripcion": (
                    "Certificacion ecologica europea "
                    "para productos agrarios y alimentarios "
                    "que cumplen la normativa aplicable."
                ),
            },
            {
                "nombre": "GOTS",
                "descripcion": (
                    "Norma para textiles fabricados con "
                    "fibras ecologicas y criterios ambientales "
                    "y sociales."
                ),
            },
            {
                "nombre": "FSC",
                "descripcion": (
                    "Certificacion relacionada con el origen "
                    "responsable de materiales forestales."
                ),
            },
            {
                "nombre": "COSMOS Organic",
                "descripcion": (
                    "Norma de certificacion para cosmetica "
                    "organica y natural."
                ),
            },
        ]

        certificaciones = {}

        for datos in certificaciones_data:
            certificacion, creada = (
                Certificacion.objects.get_or_create(
                    nombre=datos["nombre"],
                    defaults={"descripcion": datos["descripcion"]},
                )
            )
            certificaciones[certificacion.nombre] = certificacion

        # 3. Definir los 18 productos
        productos_data = [
            {
                "nombre": "Cafe molido de cooperativa",
                "descripcion": (
                    "Cafe de tueste medio, procedente de una "
                    "cooperativa de pequenos productores."
                ),
                "precio": "7.50",
                "categoria": "Cafe e infusiones",
                "certificaciones": ["Fairtrade", "Ecologico UE"],
            },
            {
                "nombre": "Cafe en grano de origen",
                "descripcion": (
                    "Cafe en grano con notas de cacao y frutos "
                    "secos, de origen responsable."
                ),
                "precio": "9.20",
                "categoria": "Cafe e infusiones",
                "certificaciones": ["Fairtrade"],
            },
            {
                "nombre": "Te verde ecologico",
                "descripcion": (
                    "Te verde de hojas seleccionadas, ideal "
                    "para disfrutar de una infusion suave."
                ),
                "precio": "4.80",
                "categoria": "Cafe e infusiones",
                "certificaciones": ["Ecologico UE"],
            },
            {
                "nombre": "Infusion de jengibre y limon",
                "descripcion": (
                    "Mezcla de plantas y especias para preparar "
                    "una infusion aromatica."
                ),
                "precio": "3.90",
                "categoria": "Cafe e infusiones",
                "certificaciones": [],
            },
            {
                "nombre": "Chocolate negro 70%",
                "descripcion": (
                    "Tableta de chocolate negro elaborada con "
                    "cacao de proveedores responsables."
                ),
                "precio": "3.25",
                "categoria": "Chocolate y dulces",
                "certificaciones": ["Fairtrade"],
            },
            {
                "nombre": "Chocolate negro ecologico",
                "descripcion": (
                    "Chocolate negro intenso elaborado con "
                    "ingredientes de produccion ecologica."
                ),
                "precio": "3.75",
                "categoria": "Chocolate y dulces",
                "certificaciones": ["Fairtrade", "Ecologico UE"],
            },
            {
                "nombre": "Tableta de chocolate con almendras",
                "descripcion": (
                    "Chocolate con almendras tostadas, "
                    "pensado para disfrutar de un dulce especial."
                ),
                "precio": "4.10",
                "categoria": "Chocolate y dulces",
                "certificaciones": ["Fairtrade"],
            },
            {
                "nombre": "Galletas de avena",
                "descripcion": (
                    "Galletas crujientes de avena para desayunos "
                    "y meriendas."
                ),
                "precio": "2.80",
                "categoria": "Alimentacion",
                "certificaciones": ["Ecologico UE"],
            },
            {
                "nombre": "Arroz integral ecologico",
                "descripcion": (
                    "Arroz integral para una alimentacion "
                    "variada y responsable."
                ),
                "precio": "2.60",
                "categoria": "Alimentacion",
                "certificaciones": ["Ecologico UE"],
            },
            {
                "nombre": "Quinoa de comercio responsable",
                "descripcion": (
                    "Quinoa versatil para ensaladas, guarniciones "
                    "y platos principales."
                ),
                "precio": "4.50",
                "categoria": "Alimentacion",
                "certificaciones": ["Fairtrade", "Ecologico UE"],
            },
            {
                "nombre": "Miel de pequenos productores",
                "descripcion": (
                    "Miel de sabor intenso presentada en un "
                    "tarro de vidrio reutilizable."
                ),
                "precio": "6.90",
                "categoria": "Alimentacion",
                "certificaciones": [],
            },
            {
                "nombre": "Camiseta de algodon ecologico",
                "descripcion": (
                    "Camiseta basica de algodon, con diseno "
                    "atemporal y produccion textil responsable."
                ),
                "precio": "18.90",
                "categoria": "Ropa y complementos",
                "certificaciones": ["GOTS"],
            },
            {
                "nombre": "Bolsa de tela reutilizable",
                "descripcion": (
                    "Bolsa resistente para reducir el uso "
                    "de bolsas desechables."
                ),
                "precio": "6.50",
                "categoria": "Ropa y complementos",
                "certificaciones": [],
            },
            {
                "nombre": "Neceser de algodon organico",
                "descripcion": (
                    "Neceser de tela para organizar productos "
                    "de higiene y cuidado personal."
                ),
                "precio": "12.00",
                "categoria": "Ropa y complementos",
                "certificaciones": ["GOTS"],
            },
            {
                "nombre": "Cuenco artesanal de madera",
                "descripcion": (
                    "Cuenco decorativo de madera para el hogar. "
                    "El origen certificado debe verificarse "
                    "en el producto comercial real."
                ),
                "precio": "14.50",
                "categoria": "Hogar",
                "certificaciones": [],
            },
            {
                "nombre": "Cuaderno de papel certificado",
                "descripcion": (
                    "Cuaderno para notas y apuntes, elaborado "
                    "con papel de origen forestal responsable."
                ),
                "precio": "5.20",
                "categoria": "Hogar",
                "certificaciones": ["FSC"],
            },
            {
                "nombre": "Jabon vegetal artesanal",
                "descripcion": (
                    "Jabon de uso diario elaborado con aceites "
                    "vegetales y presentado sin plastico innecesario."
                ),
                "precio": "4.25",
                "categoria": "Cosmetica natural",
                "certificaciones": [],
            },
            {
                "nombre": "Crema facial de aloe vera",
                "descripcion": (
                    "Crema hidratante con aloe vera para "
                    "la rutina diaria de cuidado facial."
                ),
                "precio": "11.90",
                "categoria": "Cosmetica natural",
                "certificaciones": ["COSMOS Organic"],
            },
        ]

        # 4. Crear productos y asignar sus certificaciones
        for datos in productos_data:
            producto, creado = Producto.objects.get_or_create(
                nombre=datos["nombre"],
                defaults={
                    "descripcion": datos["descripcion"],
                    "precio": Decimal(datos["precio"]),
                    "categoria": categorias[datos["categoria"]],
                },
            )

            # Si el producto ya existe, actualizamos sus datos
            # para que el comando sea repetible.
            if not creado:
                producto.descripcion = datos["descripcion"]
                producto.precio = Decimal(datos["precio"])
                producto.categoria = categorias[datos["categoria"]]
                producto.save()

            producto.certificaciones.set(
                [
                    certificaciones[nombre]
                    for nombre in datos["certificaciones"]
                ]
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Datos de prueba cargados correctamente: "
                f"{Categoria.objects.count()} categorias, "
                f"{Certificacion.objects.count()} certificaciones y "
                f"{Producto.objects.count()} productos en total."
            )
        )
