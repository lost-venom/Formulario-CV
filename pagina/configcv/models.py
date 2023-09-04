from django.db import models

class Usuario(models.Model):
    # Campos de texto
    archivo_foto = models.FileField(upload_to='documentos/', blank=True, null=True)
    numero_identificacion = models.IntegerField(unique=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    numero_celular = models.IntegerField()
    correo_electronico = models.EmailField()


    # Campos de fechas
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    formacion_academica= models.CharField(max_length=50)
    certificaciones= models.CharField(max_length=50)
    idiomas= models.CharField(max_length=50)
    habilidades= models.CharField(max_length=200)
    experiencia_laboral= models.CharField(max_length=200)
    refe_laborales= models.CharField(max_length=200)
    archivo_documento = models.FileField(upload_to='documentos/', blank=True, null=True)
    ultimo_login = models.DateTimeField(auto_now=True)
     
    # Campos booleanos
    esta_activa = models.BooleanField(default=True)
    

