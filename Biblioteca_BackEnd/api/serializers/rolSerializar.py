from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Rol
class rolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AMBU_Rol
        fields = ('id', 'rol_rol')