from django import forms
from . models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'archivo_foto',
            'numero_identificacion',
            'nombres',
            'apellidos',
            'numero_celular',
            'correo_electronico',
            'fecha_nacimiento',
            'lugar_nacimiento',
            'direccion',
            'formacion_academica',
            'certificaciones',
            'idiomas',
            'habilidades',
            'experiencia_laboral',
            'refe_laborales',
            'archivo_documento',
        ]
