# Generated by Django 4.2.4 on 2023-08-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo_foto', models.FileField(blank=True, null=True, upload_to='documentos/')),
                ('numero_identificacion', models.IntegerField(unique=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('numero_celular', models.IntegerField()),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('formacion_academica', models.CharField(max_length=50)),
                ('certificaciones', models.CharField(max_length=50)),
                ('idiomas', models.CharField(max_length=50)),
                ('habilidades', models.CharField(max_length=200)),
                ('experiencia_laboral', models.CharField(max_length=200)),
                ('refe_laborales', models.CharField(max_length=200)),
                ('archivo_documento', models.FileField(blank=True, null=True, upload_to='documentos/')),
                ('ultimo_login', models.DateTimeField(auto_now=True)),
                ('esta_activa', models.BooleanField(default=True)),
            ],
        ),
    ]
