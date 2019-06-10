from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Solicitud_Baja
from .activoSerializer import activoSerializer
from .usuarioSerializer import usuarioListSerializer
from rest_framework.validators import UniqueValidator

class solicitudBajaSerializer(serializers.ModelSerializer):

    #   CAMPOS PARA ALMACENAR ENTIDAS RELACIONADAS CON LA ENTIDAD SOLICITUD DE BAJA
    sbja_activos_modelos = serializers.SerializerMethodField('get_activos')
    sbja_usuario_modelo = serializers.SerializerMethodField('get_usuario')
    sbja_nuevoUsuario_modelo = serializers.SerializerMethodField(
        'get_usuario_nuevo')

    #   OBTIENE LOS ACTIVOS ASOCIADOS A LA SOLICITUD
    def get_activos(self, obj):
        return activoSerializer(obj.sbja_activos, many=True, read_only=True).data
    
    #   OBTIENE EL USUARIO QUE PIDIÓ LA SOLICITUD
    def get_usuario(self, obj):
        return usuarioListSerializer(obj.sbja_usuario).data
    
    #   OBTIENE EL USUARIO QUE RECIBE LA SOLICITUD
    def get_usuario_nuevo(self, obj):
        return usuarioListSerializer(obj.sbja_usuario_nuevo).data

    #   CAMPOS  A UTILIZAR EN EL JSON  
    class Meta:
        model = AMBU_Solicitud_Baja
        fields = ('id', 'sbja_fecha_solicitud', 'sbja_estado_solicitud', 'sbja_usuario', 'sbja_usuario_nuevo',
                  'sbja_activos', 'sbja_solicitud_traspaso', 'sbja_numero_formulario', 'sbja_activos_modelos',
                  'sbja_usuario_modelo', 'sbja_nuevoUsuario_modelo')

class solicitudBajaCUSerializer(serializers.ModelSerializer):

    #   VALIDACION DE CAMPOS
    #   sbja_numero_formulario -> REVISA QUE EL CAMPO SEA ÚNCO
    sbja_numero_formulario = serializers.CharField(max_length=100, 
        validators=[UniqueValidator(queryset=AMBU_Solicitud_Baja.objects.all(), 
        message="Ya existe una solicitud con ese número de formulario")])
    
    #   CAMPOS A UTILIZAR EN EL JSON
    class Meta:
        model = AMBU_Solicitud_Baja
        fields = ('id', 'sbja_fecha_solicitud', 'sbja_estado_solicitud', 'sbja_usuario', 'sbja_usuario_nuevo',
                  'sbja_activos', 'sbja_solicitud_traspaso', 'sbja_numero_formulario')

class solicitudBajaAprobar(serializers.ModelSerializer):
    
    #   CAMPOS A UTILIZAR EN EL JSON   
    class Meta:
        model = AMBU_Solicitud_Baja
        fields = ('id', 'sbja_fecha_solicitud', 'sbja_estado_solicitud',
                  'sbja_activos', 'sbja_solicitud_traspaso', 'sbja_numero_formulario')
