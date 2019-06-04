from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from Biblioteca_BackEnd.api.serializers.activoSerializer import activoSerializer, activoPUSerializer, activoBySeccionSerializer
from Biblioteca_BackEnd.api.models import AMBU_Activo
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ActivoLCView(generics.ListCreateAPIView):
    print("hola")
    #permission_classes = (IsAuthenticated,)
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

    #serializer_class = activoSerializer

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT':
            return activoPUSerializer
        else:
            return activoSerializer

class ActivoBySeccionLView(generics.ListAPIView):
   
    def get(self, request, *args, **kwargs):
        fk = kwargs.get('fk') 

        query = AMBU_Activo.objects.filter(act_seccion=fk)

        serializer = activoBySeccionSerializer(query, many=True)

        return Response(serializer.data)

class ActivoByUsuarioLView(generics.ListAPIView):
   
    def get(self, request, *args, **kwargs):
        fk = kwargs.get('fk') 

        query = AMBU_Activo.objects.filter(act_usuario_responsabe=fk)

        serializer = activoSerializer(query, many=True)

        return Response(serializer.data)

class ActivoByNumeroActivoLView(generics.ListAPIView):
   
    def get(self, request, *args, **kwargs):
        numeroActivo = kwargs.get('numeroactivo') 

        query = AMBU_Activo.objects.get(act_numero_activo=numeroActivo)

        serializer = activoSerializer(query, many=False)

        return Response(serializer.data)