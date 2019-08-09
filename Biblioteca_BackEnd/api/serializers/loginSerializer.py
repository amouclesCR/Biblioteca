from rest_framework import serializers

class loginSerializer(serializers.ModelSerializer):

    #   CAMPOS A UTILIZAR EN EL JSON
    class Meta:
        model = AMBU_Usuario
        fields = ('id', 'usu_identificacion', "usu_nombre", "usu_correo")