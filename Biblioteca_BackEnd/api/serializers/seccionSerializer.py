from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Seccion
from Biblioteca_BackEnd.api.models import AMBU_Departamento
from .departamentoSeralizer import departamentoSerializer

class seccionUCSerializer(serializers.ModelSerializer):

    class Meta:
        model = AMBU_Seccion
        fields = ('id', 'sec_nombre', 'sec_departamento')

class seccionSerializer(serializers.ModelSerializer):
    sec_departamento_modelo = serializers.SerializerMethodField('get_departamento')
    
    def get_departamento(self, obj):
        return departamentoSerializer(obj.sec_departamento).data

    class Meta:
        model = AMBU_Seccion
        fields = ('id', 'sec_nombre', 'sec_departamento', 'sec_departamento_modelo')