from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Seccion


class seccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Seccion
        fields = ('id', 'sec_nombre', 'sec_ubicacion')
