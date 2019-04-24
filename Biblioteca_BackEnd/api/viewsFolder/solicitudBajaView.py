from django.shortcuts import render
from rest_framework import generics, mixins
from Biblioteca_BackEnd.api.serializers.solicitudBajaSerializer import solicitudBajaSerializer
from Biblioteca_BackEnd.api.models import AMBU_Solicitud_Baja

class solicitudBajaLCView (generics.ListCreateAPIView):
    queryset = AMBU_Solicitud_Baja.objects.all()
    
    serializer_class = solicitudBajaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class solicitudBajaRUView (generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'

    queryset = AMBU_Solicitud_Baja.objects.all()
    
    serializer_class = solicitudBajaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
