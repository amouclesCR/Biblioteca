from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Activo
from .usuarioSerializer import usuarioBySeccioSerializer
class activoSerializer(serializers.ModelSerializer):
    #act_usuario_responsabe = usuarioSerializer(read_only=True, many=False)
    class Meta:
        model = AMBU_Activo
        fields = ('id', 
        'act_descripcion',
        'act_observacion',
        'act_numero_activo',
        'act_calor',
        'act_serie',
        'act_modelo',
        'act_marca',
        'act_estatus',
        'act_costo',
        'act_organizacion',
        'act_subestatus',
        'act_usuario_responsabe',
        'act_seccion'
        )
        depth = 1
class activoPUSerializer(serializers.ModelSerializer):
    #act_usuario_responsabe = usuarioSerializer(read_only=True, many=False)
    class Meta:
        model = AMBU_Activo
        fields = ('id', 
        'act_descripcion',
        'act_observacion',
        'act_numero_activo',
        'act_calor',
        'act_serie',
        'act_modelo',
        'act_marca',
        'act_estatus',
        'act_costo',
        'act_organizacion',
        'act_subestatus',
        'act_usuario_responsabe',
        'act_seccion'
        )

class activoBySeccionSerializer(serializers.ModelSerializer):
    act_usuario_responsabe = usuarioBySeccioSerializer(read_only=True, many=False)
    class Meta:
        model = AMBU_Activo
        fields = ('id', 
        'act_descripcion',
        'act_observacion',
        'act_numero_activo',
        'act_calor',
        'act_serie',
        'act_modelo',
        'act_marca',
        'act_estatus',
        'act_costo',
        'act_organizacion',
        'act_subestatus',
        'act_usuario_responsabe',
        )
     #   depth = 1
