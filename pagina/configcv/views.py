import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd

from .forms import UsuarioForm

def inicio(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            # Procesa los datos del formulario y guarda en la base de datos
            usuario = form.save()

            # Crea un DataFrame de pandas con los datos del usuario
            data = {
                'Número de Identificación': [usuario.numero_identificacion],
                'Nombres': [usuario.nombres],
                'Apellidos': [usuario.apellidos],
                'Número de Celular': [usuario.numero_celular],
                'Correo Electrónico': [usuario.correo_electronico],
                # Agrega más columnas según tus campos
            }
            df = pd.DataFrame(data)

            # Obtiene la ruta del archivo Excel en la carpeta media
            media_path = settings.MEDIA_ROOT
            excel_file_path = os.path.join(media_path, 'datos_registro.xlsx')

            if os.path.isfile(excel_file_path):
                # Si el archivo Excel ya existe, carga su contenido
                existing_df = pd.read_excel(excel_file_path)
                # Concatena los datos nuevos con los existentes
                df = pd.concat([existing_df, df], ignore_index=True)

            # Guarda los datos en el archivo Excel en la carpeta media
            df.to_excel(excel_file_path, index=False, engine='openpyxl')

            messages.success(request, "Datos Enviados Correctamente")

            return redirect('inicio')

    else:
        form = UsuarioForm()

    return render(request, 'inicio.html', {'form': form})
