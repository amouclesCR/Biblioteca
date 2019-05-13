from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Solicitud_Baja, AMBU_Usuario
from .activoSerializer import activoSerializer
from .usuarioSerializer  import usuarioListSerializer


class solicitudBajaSerializer(serializers.ModelSerializer):
    sbja_activos_modelos = serializers.SerializerMethodField('get_activos')
    sbja_usuario_modelo = serializers.SerializerMethodField('get_usuario')
    sbja_nuevoUsuario_modelo = serializers.SerializerMethodField('get_usuario_nuevo')

    def get_activos(self, obj):
        return activoSerializer(obj.sbja_activos, many=True, read_only=True).data

    def get_usuario(self, obj):
        return usuarioListSerializer(obj.sbja_usuario).data
    
    def get_usuario_nuevo(self, obj):
        return usuarioListSerializer(obj.sbja_usuario_nuevo).data

    class Meta:
        model = AMBU_Solicitud_Baja
        fields = ('id', 'sbja_fecha_solicitud', 'sbja_estado_solicitud', 'sbja_usuario', 'sbja_usuario_nuevo',
                  'sbja_activos', 'sbja_solicitud_traspaso', 'sbja_numero_formulario', 'sbja_activos_modelos',
                  'sbja_usuario_modelo', 'sbja_nuevoUsuario_modelo')

class solicitudBajaAprobar(serializers.ModelSerializer):

    class Meta:
        model = AMBU_Solicitud_Baja
        fields = ('id', 'sbja_fecha_solicitud', 'sbja_estado_solicitud',
                  'sbja_activos', 'sbja_solicitud_traspaso', 'sbja_numero_formulario')
