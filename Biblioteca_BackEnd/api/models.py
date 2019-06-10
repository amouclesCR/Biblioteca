from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
# Create your models here.

class AMBU_Departamento (models.Model):
    dep_nombre = models.CharField(max_length=50)

#   ALMACENA LOS DATOS DE LA ENTIDAD SECCION
class AMBU_Seccion (models.Model):
    #   ALMECENA EL NOMBRE DE LA SECCION
    sec_nombre = models.CharField(max_length=50)

#   ALMACENA LOS DATOS DE ENTIDAD ROL
class AMBU_Rol (models.Model):
    #   ALMACENA EL NOMBRE DEL ROL
    rol_rol = models.CharField(max_length=50)

#   
# class AMBU_Usuario (models.Model):
#     usu_clave = models.CharField(max_length=50)
#     usu_identificacion = models.CharField(max_length=50, unique=True)
#     usu_correo = models.CharField(max_length=50)
#     usu_nombre = models.CharField(max_length=50)
#     usu_rol = models.ForeignKey(AMBU_Rol, on_delete=models.CASCADE, default=2)
#     usu_fecha = models.DateTimeField(default=date.today)

#   USUARIO PERSONALIZADO QUE EXTIENDE A AbstractUser
class AMBU_CustomeUsuario (AbstractUser):
    pass
    #   ALMACENA LA RELACION DEL ROL
    cus_rol = models.ForeignKey(AMBU_Rol, on_delete=models.CASCADE)
    #   ALMACENA LA IDENTIFICACION DEL USUAIRO
    cus_identificacion = models.CharField(max_length=50, unique=True)

#   ALMACENA LOS DATOS DE LA ENTIDAD ACTIVOS
class AMBU_Activo (models.Model):
    #   ALMACENA LA DESCRIPCION DEL ACTIVO
    act_descripcion = models.CharField(max_length=500)
    #   ALMACENA LA OBSERVACION DEL ACTIVO
    act_observacion = models.CharField(max_length=500, blank=True)
    #   ALMACENA EL NUMERO DE ACTIVO DEL ACTIVO
    act_numero_activo = models.CharField(max_length=50, unique=True)
    #   ALMACENA EL MODELO DEL ACTIVO
    act_color = models.CharField(max_length=50)
    #   ALMACENA LA SERIE DEL ACTIVO
    act_serie = models.CharField(max_length=50)
    #   ALMACENA EL MODELO DEL ACTIVO
    act_modelo = models.CharField(max_length=50)
    #   ALMACENA LA MARCA DEL ACTIVO
    act_marca = models.CharField(max_length=50)
    #   ALMACENA EL ESTADO/ESTATUS DEL ACTIVO
    act_estatus = models.BooleanField(default=False)
    #   ALMACENA EL COSTO DEL ACTIVO
    act_costo = models.FloatField()
    #   ALMACENA LA FECHA DE SU ACTUALIZACION DEL ACTIVO
    act_Fecha_Actualizado = models.DateTimeField(default=date.today)
    #   ALMACENA LA FECHA DE CREACION DEL ACTIVO
    act_Fecha_Creacion = models.DateTimeField(default=date.today)
    #   ALMACENA LA RELACION CON EL USUARIO RESPONSABLE DEL ACTIVO
    act_usuario_responsabe = models.ForeignKey(AMBU_CustomeUsuario, on_delete=models.CASCADE)
    #   ALMACENA LA RELACION CON LA SECCION A LA QUE PERTENECE EL ACTIVO
    act_seccion = models.ForeignKey(AMBU_Seccion, on_delete=models.CASCADE)
    #act_seccione = models.ForeignKey(AMBU_Ubicacion, on_delete=models.CASCADE)

#   ALMACENA LOS DATOS DE LA SOLICITUD DE BAJA O TRASPASO
class AMBU_Solicitud_Baja (models.Model):
    #   ALMACENA LA FECHA DE CREACION DE LA SOLICITUD
    sbja_fecha_solicitud = models.DateTimeField(auto_now=True)
    #   ALMACENA EL NUMERO DE FORMULARIO
    sbja_numero_formulario = models.CharField(max_length=50, unique=True)
    #   ALMACENA EL ESTADO DE LA SOLICITUD
    #   NOTA: A = APROVADA, E = ESPERA, R = RECHAZADA
    sbja_estado_solicitud = models.CharField(max_length=1, default="E")
    #   ALMACENA EL USUARIO QUE REALIZÓ LA SOLICITUD
    sbja_usuario = models.ForeignKey(AMBU_CustomeUsuario, on_delete=models.CASCADE, null=False, related_name='entidad_usuario')
    #   ALMACENA EL USUARIO A QUE SE TRASPASA LOS ACTIVOS
    sbja_usuario_nuevo = models.ForeignKey(AMBU_CustomeUsuario, on_delete=models.CASCADE, null=True)
    #   ALMACENA LOS ACTIVOS RELACIONADOS CON LA SOLICITUD
    sbja_activos = models.ManyToManyField(AMBU_Activo, null=False)
    #   ALMACENA SI LA SOLICITUD ES DE BAJA O DE TRASPASO
    sbja_solicitud_traspaso = models.BooleanField(default=False)

class AMBU_Baja (models.Model):
    bja_motivos_solicitud = models.CharField(max_length=250)
    bja_activo = models.ForeignKey(AMBU_Activo, on_delete=models.CASCADE)
    bja_baja = models.ForeignKey(AMBU_Solicitud_Baja, on_delete=models.CASCADE)
