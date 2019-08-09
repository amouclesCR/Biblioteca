from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from Biblioteca_BackEnd.api.serializers.seccionSerializer import  seccionSerializer, seccionUCSerializer
from Biblioteca_BackEnd.api.models import AMBU_Seccion

# Create your views here.

#   LISTA Y CREA LAS SECCIONES
class SeccionLCView(generics.ListCreateAPIView):
    
    #   QUERY DE LA CONSULTA
    queryset = AMBU_Seccion.objects.all()
    
    #   MAPEA LOS DATOS
    serializer_class = seccionSerializer

    def get_serializer_class(self):

        #   SI EL METODO ES POST USA seccionUCSerializer
        method = self.request.method
        if method == 'POST':
            return seccionUCSerializer
        else:
            return seccionSerializer

#   OBTIENE O ACTUALIZA UNA SECCIO 
class SeccionRUView(generics.RetrieveUpdateAPIView):
    
    #   OBTIENE LA PK DE LA URL
    lookup_field = 'pk' 
    
    #   CONSULTA
    queryset = AMBU_Seccion.objects.all()
    
    #   MAPEA LOS DATOS
    serializer_class = seccionSerializer

    def get_serializer_class(self):

        #   SI EL METODO ES PUT UTILIZA seccionUCSerializer
        method = self.request.method
        if method == 'PUT':
            return seccionUCSerializer
        else:
            return seccionSerializer