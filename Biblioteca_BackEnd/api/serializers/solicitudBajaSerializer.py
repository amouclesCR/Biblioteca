from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Solicitud_Baja
from .usuarioSerializer import usuarioSerializer

class solicitudBajaSerializer(serializers.ModelSerializer):
    sbja_usuarioEntity = usuarioSerializer(many=True, read_only=True)
    class Meta:
        model = AMBU_Solicitud_Baja
        fields = ('id', 'sbja_fecha_solicitud', 'sbja_estado_solicitud', 'sbja_usuario', 'sbja_usuarioEntity')