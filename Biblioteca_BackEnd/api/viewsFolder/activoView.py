from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from Biblioteca_BackEnd.api.serializers.activoSerializer import activoSerializer
from Biblioteca_BackEnd.api.models import AMBU_Activo

# Create your views here.
class ActivoLCView(generics.ListCreateAPIView):
    
    queryset = AMBU_Activo.objects.all()
    
    serializer_class = activoSerializer

class ActivoRUView(generics.RetrieveUpdateAPIView):
   
    lookup_field = 'pk' # PRIMARY KEY FROM URL
    
    queryset = AMBU_Activo.objects.all()

    serializer_class = activoSerializer

    def get_queryset(self):
        return AMBU_Activo.objects.all()