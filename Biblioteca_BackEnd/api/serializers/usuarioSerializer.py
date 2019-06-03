from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Usuario, AMBU_CustomeUsuario
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

class usuarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('usu_identificacion', "usu_nombre", "usu_correo", "usu_clave")

class usuarioBySeccioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id', 'usu_identificacion')

class recoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Usuario
        fields = ('id','usu_identificacion', "usu_correo", "usu_clave")

class customSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('username', 'first_name', 'email', 'password')

    def create(self, validated_data):
        user = AMBU_CustomeUsuario(email=validated_data['email'], username=validated_data['username'])
        
        user.set_password(validated_data['password'])
        user.save()
        return user