from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Activo, AMBU_Usuario
from .usuarioSerializer import usuarioBySeccioSerializer
from .seccionSerializer import seccionSerializer
from rest_framework.validators import UniqueValidator

class activoSerializer(serializers.ModelSerializer):
    #act_usuario_responsabe = usuarioSerializer(read_only=True, many=False)
    act_usuario = serializers.SerializerMethodField('get_usuario_responsable')
    act_seccion_modelo = serializers.SerializerMethodField('get_seccion')
    
    def get_usuario_responsable(self, obj):
        return usuarioBySeccioSerializer(obj.act_usuario_responsabe).data

    def get_seccion(self, obj):
        return seccionSerializer(obj.act_seccion).data
    
    class Meta:
        model = AMBU_Activo
        fields = ('id', 
        'act_descripcion',
        'act_observacion',
        'act_numero_activo',
        'act_color',
        'act_serie',
        'act_modelo',
        'act_marca',
        'act_estatus',
        'act_costo',
        'act_usuario_responsabe',
        'act_usuario',
        'act_seccion',
        'act_seccion_modelo',
        'act_Fecha_Creacion'
        )
class activoPUSerializer(serializers.ModelSerializer):

    #   VALIDACIONES DE CAMPOS
    act_numero_activo = serializers.CharField(max_length=100, 
        validators=[UniqueValidator(queryset=AMBU_Activo.objects.all(), 
        message="Ya existe un activo con ese número de activo")])

    #   CAMPOS DEL JSON
    class Meta:
        model = AMBU_Activo
        fields = ('id', 
        'act_descripcion',
        'act_observacion',
        'act_numero_activo',
        'act_color',
        'act_serie',
        'act_modelo',
        'act_marca',
        'act_estatus',
        'act_costo',
        'act_usuario_responsabe',
        'act_seccion'
        )

class activoBySeccionSerializer(serializers.ModelSerializer):
    act_usuario = serializers.SerializerMethodField('get_usuario_responsable')

    def get_usuario_responsable(self, obj):
        return usuarioBySeccioSerializer(obj.act_usuario_responsabe).data
    class Meta:
        model = AMBU_Activo
        fields = ('id', 
        'act_descripcion',
        'act_observacion',
        'act_numero_activo',
        'act_color',
        'act_serie',
        'act_modelo',
        'act_marca',
        'act_estatus',
        'act_costo',
        'act_usuario_responsabe',
        'act_usuario',
        'act_Fecha_Creacion'
        )
     #   depth = 1
