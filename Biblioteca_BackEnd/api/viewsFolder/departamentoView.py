from django.shortcuts import render
from rest_framework import generics, mixins
from Biblioteca_BackEnd.api.serializers.departamentoSeralizer import departamentoSerializer 
from Biblioteca_BackEnd.api.models import AMBU_Departamento, AMBU_Activo

class departamentoLCView (generics.ListCreateAPIView):
    queryset = AMBU_Departamento.objects.all()
    
    serializer_class = departamentoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class departamentoRUView (generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'

    queryset = AMBU_Departamento.objects.all()
    
    serializer_class = departamentoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
