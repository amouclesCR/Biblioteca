from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from Biblioteca_BackEnd.api.serializers.serializer import  seccionSerializer
from Biblioteca_BackEnd.api.models import AMBU_Seccion
from django.db.models import Count
# Create your views here.
class SeccionLCView(generics.ListCreateAPIView):
    
    queryset = AMBU_Seccion.objects.all()
    
    serializer_class = seccionSerializer

class SeccionRUView(generics.RetrieveUpdateAPIView):
   
    lookup_field = 'pk' # PRIMARY KEY FROM URL
    
    queryset = AMBU_Seccion.objects.all()

    serializer_class = seccionSerializer

    def get_queryset(self):
        return AMBU_Seccion.objects.all()