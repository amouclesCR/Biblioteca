from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_CustomeUsuario
from .rolSerializar import rolSerializer


class usuarioListSerializer(serializers.ModelSerializer):
    cus_rol_modelo = serializers.SerializerMethodField('get_rol')

    def get_rol(self, obj):
        return rolSerializer(obj.cus_rol, read_only=True).data

    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('id', 'cus_identificacion', "email",
                  "cus_rol", "cus_rol_modelo")


class usuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('id', 'cus_identificacion', "email",
                  "cus_rol", "cus_rol_modelo")


class usuarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('cus_identificacion', "email", "password")


class usuarioBySeccioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('id', 'cus_identificacion')


class recoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('id', 'cus_identificacion', "email", "password")


class customSerializer(serializers.ModelSerializer):
    cus_rol_modelo = serializers.SerializerMethodField('get_rol')

    def get_rol(self, obj):
        return rolSerializer(obj.cus_rol, read_only=True).data

    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('id', 'username', 'first_name', 'email',
                  "cus_rol", 'cus_identificacion', 'cus_rol_modelo')


class customUserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('username', 'email', 'cus_identificacion', 'password')

    def create(self, validated_data):
        user = AMBU_CustomeUsuario(
            email=validated_data['email'], username=validated_data['username'], cus_identificacion=validated_data['cus_identificacion'])
        user.set_password(validated_data['password'])
        user.save()
        return user
