from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from Biblioteca_BackEnd.api.serializers.bajaSerializer import bajaSerializer
from Biblioteca_BackEnd.api.models import AMBU_Baja

# Create your views here.
class BajaLCView(generics.ListCreateAPIView):
    
    queryset = AMBU_Baja.objects.all()
    
    serializer_class = bajaSerializer

class BajaRUView(generics.RetrieveUpdateAPIView):
   
    lookup_field = 'pk' # PRIMARY KEY FROM URL
    
    queryset = AMBU_Baja.objects.all()

    serializer_class = bajaSerializer

    def get_queryset(self):
        return AMBU_Baja.objects.all()