from rest_framework import serializers
from Biblioteca_BackEnd.api.models import AMBU_Baja


class bajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMBU_Baja
        fields = ('id', 'bja_activo', 'bja_baja', 'bja_motivos_solicitud')
