from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
# Create your models here.

class AMBU_Departamento (models.Model):
    dep_nombre = models.CharField(max_length=50)

class AMBU_Seccion (models.Model):
    sec_nombre = models.CharField(max_length=50)
    # sec_departamento = models.ForeignKey(AMBU_Departamento, on_delete=models.CASCADE)

class AMBU_Rol (models.Model):
        rol_rol = models.CharField(max_length=50)

class AMBU_Usuario (models.Model):
    usu_clave = models.CharField(max_length=50)
    usu_identificacion = models.CharField(max_length=50, unique=True)
    usu_correo = models.CharField(max_length=50)
    usu_nombre = models.CharField(max_length=50)
    usu_rol = models.ForeignKey(AMBU_Rol, on_delete=models.CASCADE, default=2)
    usu_fecha = models.DateTimeField(default=date.today)

class AMBU_CustomeUsuario (AbstractUser):
    pass
    name = models.CharField(max_length=50)
    cus_rol = models.ForeignKey(AMBU_Rol, on_delete=models.CASCADE, default=2)
    cus_identificacion = models.CharField(max_length=50, unique=True)

class AMBU_Activo (models.Model):
    act_descripcion = models.CharField(max_length=500)
    act_observacion = models.CharField(max_length=500, blank=True)
    act_numero_activo = models.CharField(max_length=50)
    act_color = models.CharField(max_length=50)
    act_serie = models.CharField(max_length=50)
    act_modelo = models.CharField(max_length=50)
    act_marca = models.CharField(max_length=50)
    act_estatus = models.BooleanField(default=False)
    act_costo = models.FloatField()
    act_Fecha_Actualizado = models.DateTimeField(default=date.today)
    act_Fecha_Creacion = models.DateTimeField(default=date.today)
    act_usuario_responsabe = models.ForeignKey(AMBU_CustomeUsuario, on_delete=models.CASCADE)
    act_seccion = models.ForeignKey(AMBU_Seccion, on_delete=models.CASCADE)
    #act_seccione = models.ForeignKey(AMBU_Ubicacion, on_delete=models.CASCADE)

class AMBU_Solicitud_Baja (models.Model):
    sbja_fecha_solicitud = models.DateTimeField(auto_now=True)
    sbja_numero_formulario = models.CharField(max_length=50)
    sbja_estado_solicitud = models.CharField(max_length=1, default="E")
    sbja_usuario = models.ForeignKey(AMBU_CustomeUsuario, on_delete=models.CASCADE, null=False, related_name='entidad_usuario')
    sbja_usuario_nuevo = models.ForeignKey(AMBU_CustomeUsuario, on_delete=models.CASCADE, null=True)
    sbja_activos = models.ManyToManyField(AMBU_Activo, null=False)
    sbja_solicitud_traspaso = models.BooleanField(default=False)

class AMBU_Baja (models.Model):
    bja_motivos_solicitud = models.CharField(max_length=250)
    bja_activo = models.ForeignKey(AMBU_Activo, on_delete=models.CASCADE)
    bja_baja = models.ForeignKey(AMBU_Solicitud_Baja, on_delete=models.CASCADE)
