from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Departamento

class departamentoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = AMBU_Departamento
        fields = ('id', 'dep_nombre')