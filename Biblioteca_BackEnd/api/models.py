from django.db import models

# Create your models here.

class AMBU_Seccion (models.Model):
    sec_nombre = models.CharField(max_length=50)
    sec_ubicacion = models.CharField(max_length=250, null=True)

class AMBU_Usuario (models.Model):
    usu_nombre_usuario = models.CharField(max_length=50)
    usu_clave = models.CharField(max_length=50)
    usu_nombre = models.CharField(max_length=50)
    usu_apellidos = models.CharField(max_length=50)
    usu_identificacion = models.CharField(max_length=50)

class AMBU_Solicitud_Baja (models.Model):
    sbja_fecha_solicitud = models.DateField(auto_now=False)
    sbja_estado_solicitud = models.BooleanField(default=False)
    sbja_usuario = models.ForeignKey(AMBU_Usuario, on_delete=models.CASCADE, null=False, related_name='entidad_usuario')

class AMBU_Activo (models.Model):
    act_descripcion = models.CharField(max_length=500)
    act_observacion = models.CharField(max_length=500)
    act_numero_activo = models.CharField(max_length=50)
    act_calor = models.CharField(max_length=50)
    act_serie = models.CharField(max_length=50)
    act_modelo = models.CharField(max_length=50)
    act_marca = models.CharField(max_length=50)
    act_estatus = models.BooleanField(default=False)
    act_costo = models.FloatField()
    act_organizacion = models.CharField(max_length=50)
    act_subestatus = models.CharField(max_length=50, null=True)
    act_usuario_responsabe = models.ForeignKey(AMBU_Usuario, on_delete=models.CASCADE)
    act_seccion = models.ForeignKey(AMBU_Seccion, on_delete=models.CASCADE)

class AMBU_Baja (models.Model):
    bja_motivos_solicitud = models.CharField(max_length=250)
    bja_activo = models.ForeignKey(AMBU_Activo, on_delete=models.CASCADE)
    bja_baja = models.ForeignKey(AMBU_Solicitud_Baja, on_delete=models.CASCADE)