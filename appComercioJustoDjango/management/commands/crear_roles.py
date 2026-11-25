from django.contrib.auth.models import Group, Permission, User
from django.core.management.base import BaseCommand
from django.db import transaction

ROLES = {
    'Gestor de catálogo': {
        'producto': ['add', 'change', 'delete', 'view'],
        'categoria': ['add', 'change', 'delete', 'view'],
        'certificacion': ['add', 'change', 'delete', 'view'],
    },
    'Atención al cliente': {
        'consulta': ['change', 'delete', 'view'],
        'producto': ['view'],
    },
}

USUARIOS_DEMO = [
    ('gestor', 'Gestor de catálogo'),
    ('atencion', 'Atención al cliente'),
]


class Command(BaseCommand):
    help = 'Crea los grupos de administradores con sus permisos y un usuario de prueba por rol'

    def add_arguments(self, parser):
        parser.add_argument('--sin-usuarios', action='store_true', help='Solo crea los grupos')
        parser.add_argument('--password', default='ComercioJusto2026', help='Contraseña de los usuarios de prueba')

    @transaction.atomic
    def handle(self, *args, **options):
        for nombre_grupo, modelos in ROLES.items():
            grupo, _ = Group.objects.get_or_create(name=nombre_grupo)
            codenames = [f'{accion}_{modelo}' for modelo, acciones in modelos.items() for accion in acciones]
            permisos = Permission.objects.filter(
                content_type__app_label='appComercioJustoDjango', codename__in=codenames
            )
            grupo.permissions.set(permisos)
            self.stdout.write(self.style.SUCCESS(f'Grupo "{nombre_grupo}": {permisos.count()} permisos'))

        if options['sin_usuarios']:
            return

        for username, nombre_grupo in USUARIOS_DEMO:
            usuario, creado = User.objects.get_or_create(username=username, defaults={'is_staff': True})
            if creado:
                usuario.set_password(options['password'])
                usuario.save()
            usuario.groups.set([Group.objects.get(name=nombre_grupo)])
            estado = 'creado' if creado else 'ya existía'
            self.stdout.write(self.style.SUCCESS(f'Usuario "{username}" ({nombre_grupo}) {estado}'))
