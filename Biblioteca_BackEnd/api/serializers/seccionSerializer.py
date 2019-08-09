from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Seccion
from rest_framework.validators import UniqueValidator

class seccionUCSerializer(serializers.ModelSerializer):

    #   VALIDACION DE CAMPOS
    #   sec_nombre -> VALIDA QUE EL CAMPO SEA ÚNICO
    sec_nombre= serializers.CharField(max_length=100, 
        validators=[UniqueValidator(queryset=AMBU_Seccion.objects.all(), 
        message="Ya existe una sección con ese nombre")])

    #   CAMPOS A UTILIZAR EN EL JSON
    class Meta:
        model = AMBU_Seccion
        fields = ('id', 'sec_nombre')

class seccionSerializer(serializers.ModelSerializer):
    
    #   CAMPOS A UTILIZAR EN EL JSON
    class Meta:
        model = AMBU_Seccion
        fields = ('id', 'sec_nombre')