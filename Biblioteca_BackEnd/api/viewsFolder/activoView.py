from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from Biblioteca_BackEnd.api.serializers.activoSerializer import activoSerializer, activoPUSerializer, activoBySeccionSerializer
from Biblioteca_BackEnd.api.models import AMBU_Activo
from rest_framework.permissions import IsAuthenticated

# Create your views here.

#   LISTA Y LOS CREA LOS ACTIVOS
class ActivoLCView(generics.ListCreateAPIView):
    #   QUERY DE LA CONSULTA
    queryset = AMBU_Activo.objects.all()
    
    #   OBTIENE EL SERIALIZER PARA DEVOLVER LOS DATOS
    def get_serializer_class(self):
        #   SI EL METODO ES POST UTILIZA activoPUSerializer
        method = self.request.method
        if method == 'POST':
            return activoPUSerializer
        else:
            return activoSerializer

#   ACTUALIZA O DEVUELVE UN ACTIVO
class ActivoRUView(generics.RetrieveUpdateAPIView):

    #   PRIMARY KEY EN LA URL
    lookup_field = 'pk'
    
    #   QUERY DE LA CONSULTA
    queryset = AMBU_Activo.objects.all()

    #   OBTIENE EL SERIALIZER PARA DEVOLVER LOS DATOS
    def get_serializer_class(self):
        #   SI EL METODO ES PUT UTILIZA activoPUSerializer
        method = self.request.method
        if method == 'PUT':
            return activoPUSerializer
        else:
            return activoSerializer

#   OBTIENE LOS ACTIVOS SEGÚN LA SECCIÓN
class ActivoBySeccionLView(generics.ListAPIView):
   
    def get(self, request, *args, **kwargs):
        
        #   OBTIENE EL ID/FK DE LA RUTA/URL
        fk = kwargs.get('fk') 

        #   QUERY DE LA CONSULTA
        query = AMBU_Activo.objects.filter(act_seccion=fk)

        # MAPEA LOS DATOS 
        serializer = activoBySeccionSerializer(query, many=True)

        return Response(serializer.data)

#   OBTIENE LOS ACTIVOS SEGÚN EL USUARIO
class ActivoByUsuarioLView(generics.ListAPIView):
   
    def get(self, request, *args, **kwargs):

        #   OBTIENE EL ID/FK DE LA RUTA/URL
        fk = kwargs.get('fk') 

        #   QUERY DE LA CONSULTA
        query = AMBU_Activo.objects.filter(act_usuario_responsabe=fk)
        
        # MAPEA LOS DATOS 
        serializer = activoSerializer(query, many=True)

        return Response(serializer.data)

#   OBTIENE EL ACTIVOS SEGÚN EL NÚMERO DE ACTIVO
class ActivoByNumeroActivoLView(generics.ListAPIView):
   
    def get(self, request, *args, **kwargs):

        #   OBTIENE EL NUMERO DE ACTIVO "numeroactivo" DE LA URL
        numeroActivo = kwargs.get('numeroactivo') 

        #   QUERY DE LA CONSULTA
        query = AMBU_Activo.objects.get(act_numero_activo=numeroActivo)

        #   MAPEA LOS DATOS
        serializer = activoSerializer(query, many=False)

        return Response(serializer.data)