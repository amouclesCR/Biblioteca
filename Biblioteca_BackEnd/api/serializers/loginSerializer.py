from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Usuario

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id', 'usu_nombre_usuario', 'usu_nombre', 'usu_apellidos', 'usu_identificacion')