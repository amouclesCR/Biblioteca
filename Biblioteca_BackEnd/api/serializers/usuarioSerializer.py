from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Usuario

class usuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id','usu_identificacion', "usu_nombre", "usu_correo")

class usuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id', 'usu_identificacion', "usu_nombre", "usu_correo")

class usuarioBySeccioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id', 'usu_identificacion')