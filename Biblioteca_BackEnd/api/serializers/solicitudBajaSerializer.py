from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Solicitud_Baja, AMBU_Usuario
from .usuarioSerializer import usuarioListSerializer

class solicitudBajaSerializer(serializers.ModelSerializer):
    entidad_usuario = usuarioListSerializer(read_only=True, many=False)
   # print(AMBU_Solicitud_Baja.sbja_usuario)
    #entidad_usuario = serializers.HyperlinkedRelatedField(read_only=True, view_name='usuario-lc')
    #entidad_usuarioId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=AMBU_Usuario.objects.all(), source='sbja_usuario')
    class Meta:
        model = AMBU_Solicitud_Baja
        fields = ('id', 'sbja_fecha_solicitud', 'sbja_estado_solicitud', 'sbja_usuario', 'entidad_usuario')
        depth = 1