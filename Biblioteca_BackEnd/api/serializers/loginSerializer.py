from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Usuario

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id', 'usu_identificacion', "usu_nombre", "usu_correo")