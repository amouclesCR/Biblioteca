from django.shortcuts import render
from rest_framework import generics, mixins
from Biblioteca_BackEnd.api.serializers.usuarioSerializer import usuarioListSerializer, usuarioUpdateSerializer
from Biblioteca_BackEnd.api.models import AMBU_Usuario

class usuarioLCView (generics.ListCreateAPIView):
    queryset = AMBU_Usuario.objects.all()
    
    serializer_class = usuarioListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class usuarioRUView (generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'

    queryset = AMBU_Usuario.objects.all()
    
    serializer_class = usuarioListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)