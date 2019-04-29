from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Usuario

class usuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id', 'usu_nombre_usuario', 'usu_nombre', 'usu_apellidos', 'usu_identificacion')

class usuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id', 'usu_nombre_usuario', 'usu_clave', 'usu_nombre', 'usu_apellidos', 'usu_identificacion')

class usuarioBySeccioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id', 'usu_nombre')