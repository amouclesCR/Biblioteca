from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Seccion
from Biblioteca_BackEnd.api.models import AMBU_Departamento
from .departamentoSeralizer import departamentoSerializer

class seccionUCSerializer(serializers.ModelSerializer):

    class Meta:
        model = AMBU_Seccion
        fields = ('id', 'sec_nombre')

class seccionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AMBU_Seccion
        fields = ('id', 'sec_nombre')