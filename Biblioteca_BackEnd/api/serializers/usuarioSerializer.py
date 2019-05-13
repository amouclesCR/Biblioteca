from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Usuario
from .rolSerializar import rolSerializer

class usuarioListSerializer(serializers.ModelSerializer):
    usu_rol_modelo = serializers.SerializerMethodField('get_rol')

    def get_rol(self, obj):
        return rolSerializer(obj.usu_rol, read_only=True).data

    class Meta:
        model = AMBU_Usuario
        fields = ('id','usu_identificacion', "usu_nombre", "usu_correo", "usu_rol", "usu_rol_modelo")

class usuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id', 'usu_identificacion', "usu_nombre", "usu_correo", "usu_rol", "usu_rol_modelo")

class usuarioBySeccioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id', 'usu_identificacion')