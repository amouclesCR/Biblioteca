from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from Biblioteca_BackEnd.api.serializers.activoSerializer import activoSerializer, activoPUSerializer, activoBySeccionSerializer
from Biblioteca_BackEnd.api.models import AMBU_Activo

# Create your views here.
class ActivoLCView(generics.ListCreateAPIView):
    
    queryset = AMBU_Activo.objects.all()
    
    #serializer_class = activoSerializer

    def get_serializer_class(self):
        method = self.request.method
        if method == 'POST':
            return activoPUSerializer
        else:
            return activoSerializer

class ActivoRUView(generics.RetrieveUpdateAPIView):
   
    lookup_field = 'pk' # PRIMARY KEY FROM URL
    
    queryset = AMBU_Activo.objects.all()

    serializer_class = activoSerializer

    def get_queryset(self):
        return AMBU_Activo.objects.all()

class ActivoBySeccionLView(generics.ListAPIView):
   
    def get(self, request, *args, **kwargs):
        fk = kwargs.get('fk') 

        query = AMBU_Activo.objects.filter(act_seccion=fk)

        serializer = activoBySeccionSerializer(query, many=True)

        return Response(serializer.data)