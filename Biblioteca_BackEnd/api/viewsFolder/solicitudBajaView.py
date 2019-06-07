from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework import status
from django.db.models import Q
import json
from Biblioteca_BackEnd.api.serializers.solicitudBajaSerializer import solicitudBajaSerializer, solicitudBajaAprobar, solicitudBajaCUSerializer
from Biblioteca_BackEnd.api.models import AMBU_Solicitud_Baja, AMBU_Activo

class solicitudBajaLCView (generics.ListCreateAPIView):
    queryset = AMBU_Solicitud_Baja.objects.all()
    
    def get_serializer_class(self):
        method = self.request.method
        if method == 'POST':
            return solicitudBajaCUSerializer
        else:
            return solicitudBajaSerializer

class solicitudBajaLView (generics.ListAPIView):
    queryset = AMBU_Solicitud_Baja.objects.filter(sbja_estado_solicitud="E")
    
    serializer_class = solicitudBajaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class solicitudBajaRUView (generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'

    queryset = AMBU_Solicitud_Baja.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT':
            return solicitudBajaCUSerializer
        else:
            return solicitudBajaSerializer
        
class solicitudByUsuarioL(generics.ListAPIView):
   
    def get(self, request, *args, **kwargs):
        fk = kwargs.get('pk') 

        query = AMBU_Solicitud_Baja.objects.filter(sbja_usuario=fk)

        serializer = solicitudBajaSerializer(query, many=True)

        return Response(serializer.data)

class solicitudAprobar(generics.UpdateAPIView):
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk') 
        query = AMBU_Solicitud_Baja.objects.get(id=pk)
        query.sbja_estado_solicitud = "A"
        activos = AMBU_Solicitud_Baja.objects.filter(id=pk).values_list('sbja_activos')
        
        if (activos[0][0] != None and len(activos[0]) > 0):
            for ac in activos:
                activo = AMBU_Activo.objects.get(id=ac[0])
                if (query.sbja_solicitud_traspaso):
                    activo.act_usuario_responsabe = query.sbja_usuario_nuevo
                else:
                    activo.act_estatus = False
                activo.save()
        else:
            return Response("No se han encontrado activos en la solicitud", status=status.HTTP_400_BAD_REQUEST)   
        query.save()
        return Response(status=status.HTTP_200_OK)

class solicitudRechazar(generics.UpdateAPIView):
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk') 
        query = AMBU_Solicitud_Baja.objects.get(id=pk)

        if query is None:
            return Response("No se ha encontrado la solicitud", status=status.HTTP_400_BAD_REQUEST)   

        query.sbja_estado_solicitud = "R"
        query.save()
        return Response(status=status.HTTP_200_OK)