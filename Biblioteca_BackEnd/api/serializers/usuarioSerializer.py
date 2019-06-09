from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_CustomeUsuario
from .rolSerializar import rolSerializer
from rest_framework.validators import UniqueValidator

class usuarioListSerializer(serializers.ModelSerializer):

    #   CAMPOS PARA ALMACENAR ENTIDAS RELACIONADAS CON LA ENTIDAD USUARIO
    cus_rol_modelo = serializers.SerializerMethodField('get_rol')

    #   OBTIENE EL ROL ASOCIADO AL USUARIO
    def get_rol(self, obj):
        return rolSerializer(obj.cus_rol, read_only=True).data

    #   CAMPOS A UTILIZAR EN EL JSON    
    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('id', 'cus_identificacion', "email",
                  "cus_rol", "cus_rol_modelo", 'first_name', 'date_joined')

class usuarioBySeccioSerializer(serializers.ModelSerializer):
    
    #   CAMPOS A UTILIZAR EN EL JSON
    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('id', 'cus_identificacion')

class recoverySerializer(serializers.ModelSerializer):
    
    #   CAMPOS A UTILIZAR EN EL JSON
    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('id', 'cus_identificacion', "email", "password")

class customSerializer(serializers.ModelSerializer):

    #   CAMPOS PARA ALMACENAR ENTIDAS RELACIONADAS CON LA ENTIDAD USUARIO
    cus_rol_modelo = serializers.SerializerMethodField('get_rol')

    #   OBTIENE EL ROL ASOCIADO AL USUARIO
    def get_rol(self, obj):
        return rolSerializer(obj.cus_rol, read_only=True).data

    #   CAMPOS A UTILIZAR EN EL JSON
    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('id', 'username', 'first_name', 'email',
                  "cus_rol", 'cus_identificacion', 'cus_rol_modelo')


class customUserRegisterSerializer(serializers.ModelSerializer):

    #   VALIDACIONES DE CAMPOS
    cus_identificacion = serializers.CharField(max_length=100, 
        validators=[UniqueValidator(queryset=AMBU_CustomeUsuario.objects.all(), 
        message="Ya existe un usuario con esa identificación")])
    username = serializers.CharField(max_length=100, 
        validators=[UniqueValidator(queryset=AMBU_CustomeUsuario.objects.all(),
        message="Ya existe un usuario con ese nombre de usuario")])
    email = serializers.CharField(max_length=100, 
        validators=[UniqueValidator(queryset=AMBU_CustomeUsuario.objects.all(),
        message="Ya existe un usuario con ese correo")])
    
    #   CAMPOS A UTILIZAR EN EL JSON
    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('username', 'email', 'cus_identificacion',
                  'password', 'first_name')

    #   CREA EL USUARIO Y ASIGNA LA CONTRASEÑA ENCRIPTIADA
    def create(self, validated_data):
        user = AMBU_CustomeUsuario(
            email=validated_data['email'], username=validated_data['username'], cus_identificacion=validated_data['cus_identificacion'], first_name=validated_data['first_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
