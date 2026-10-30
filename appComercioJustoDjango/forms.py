from django import forms

from .models import Consulta


class ConsultaForm(forms.ModelForm):

    privacidad = forms.BooleanField(
        required=True,
        label='Acepto la política de privacidad',
        error_messages={'required': 'Debes aceptar la política de privacidad.'},
    )

    class Meta:
        model = Consulta
        fields = ['nombre', 'correo_electronico', 'telefono', 'perfil', 'interes', 'mensaje', 'privacidad']
        labels = {
            'nombre': 'Nombre y apellidos',
            'correo_electronico': 'Email',
            'telefono': 'Teléfono',
            'perfil': '¿Eres consumidor o productor?',
            'interes': 'Producto de interés',
            'mensaje': 'Mensaje',
        }
        widgets = {
            'perfil': forms.RadioSelect,
            'mensaje': forms.Textarea(attrs={'rows': 6, 'cols': 50}),
        }