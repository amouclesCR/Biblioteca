from django.contrib import admin
from Biblioteca_BackEnd.api.models import AMBU_Seccion, AMBU_Solicitud_Baja, AMBU_Activo, AMBU_Baja
                                         
# Register your models here.

admin.site.register(AMBU_Seccion)
admin.site.register(AMBU_Solicitud_Baja)
admin.site.register(AMBU_Activo)
admin.site.register(AMBU_Baja)