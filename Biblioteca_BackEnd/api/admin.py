from django.contrib import admin
from Biblioteca_BackEnd.api.models import AMBU_Seccion, AMBU_Usuario, AMBU_Solicitud_Baja, AMBU_Activo
                                         
# Register your models here.

admin.site.register(AMBU_Seccion)
admin.site.register(AMBU_Usuario)
admin.site.register(AMBU_Solicitud_Baja)
admin.site.register(AMBU_Activo)