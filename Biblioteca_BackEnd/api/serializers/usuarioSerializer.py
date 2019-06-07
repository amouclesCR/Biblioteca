from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_CustomeUsuario
from .rolSerializar import rolSerializer
from rest_framework.validators import UniqueValidator

class usuarioListSerializer(serializers.ModelSerializer):
    cus_rol_modelo = serializers.SerializerMethodField('get_rol')

    def get_rol(self, obj):
        return rolSerializer(obj.cus_rol, read_only=True).data

    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('id', 'cus_identificacion', "email",
                  "cus_rol", "cus_rol_modelo", 'first_name')


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
    cus_identificacion = serializers.CharField(max_length=100, 
        validators=[UniqueValidator(queryset=AMBU_CustomeUsuario.objects.all(), 
        message="identificacion debe ser unica")])
    username = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=AMBU_CustomeUsuario.objects.all(), message="unico")])
    class Meta:
        model = AMBU_CustomeUsuario
        fields = ('username', 'email', 'cus_identificacion',
                  'password', 'first_name')
        #extra_kwargs = {"username": {"validators": [validate]}}
    # def validate_cus_identificacion(self, attrs):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     print("siiiii")
    #     value = "dLjango"
    #     if "django" not in value.lower():
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     return attrs
    # def validate_username(self, attrs):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     print("siiiii")
    #     value = "dLjango" 
    #     if "django" not in value.lower():
    #         raise serializers.ValidationError("Usuario ocupado")
    #     return attrs
    def create(self, validated_data):
        user = AMBU_CustomeUsuario(
            email=validated_data['email'], username=validated_data['username'], cus_identificacion=validated_data['cus_identificacion'], first_name=validated_data['first_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
