from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework import status
from django.db.models import Q
import json
from Biblioteca_BackEnd.api.serializers.solicitudBajaSerializer import solicitudBajaSerializer, solicitudBajaAprobar, solicitudBajaCUSerializer
from Biblioteca_BackEnd.api.models import AMBU_Solicitud_Baja, AMBU_Activo

#   LISTA O CREA LAS SOLICITUDES
class solicitudBajaLCView (generics.ListCreateAPIView):
    
    #   CONSULTA
    queryset = AMBU_Solicitud_Baja.objects.all()
    
    def get_serializer_class(self):
        
        #   SI EL METODO ES POST UTILIZA solicitudBajaCUSerializer
        method = self.request.method
        if method == 'POST':
            return solicitudBajaCUSerializer
        else:
            return solicitudBajaSerializer

#   OBTIENE LAS SOLICITUDES CON ESTADO DE ESPERA
class solicitudBajaLView (generics.ListAPIView):

    #   CONSULTA
    queryset = AMBU_Solicitud_Baja.objects.filter(sbja_estado_solicitud="E")
    
    #   MAPEA LOS DATOS
    serializer_class = solicitudBajaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

#   OBTIENE O ACTUALIZA UNA SOLICITUD
class solicitudBajaRUView (generics.RetrieveUpdateAPIView):

    #   OBTIENE LA PK DE LA URL
    lookup_field = 'pk'

    #   CONSULTA
    queryset = AMBU_Solicitud_Baja.objects.all()

    def get_serializer_class(self):

        #   SI EL METODO ES PUT UTILIZA solicitudBajaCUSerializer
        method = self.request.method
        if method == 'PUT':
            return solicitudBajaCUSerializer
        else:
            return solicitudBajaSerializer
        
#   OBTIENEN LAS SOLICITUDES REALIZADAS POR USUARIO
class solicitudByUsuarioL(generics.ListAPIView):
   
    def get(self, request, *args, **kwargs):

        #   OBTIENE LA PK DE LA RUTA
        fk = kwargs.get('pk') 

        #   CONSULTA
        query = AMBU_Solicitud_Baja.objects.filter(sbja_usuario=fk)

        #   MAPEA LOS DATOS
        serializer = solicitudBajaSerializer(query, many=True)

        return Response(serializer.data)

#   APRUEBA LA SOLICITUD
class solicitudAprobar(generics.UpdateAPIView):
    
    def put(self, request, *args, **kwargs):

        #   OBTIENE LA PK DE LA RUTA
        pk = kwargs.get('pk') 

        # CONSULTA
        query = AMBU_Solicitud_Baja.objects.get(id=pk)
        # SE CAMBIA EL ESTADO DE LA SOLICITUD
        query.sbja_estado_solicitud = "A"
        
        #   SE OBTIENEN LAS SOLICITUDES 
        #   NOTA: TRAE TUPLAS
        activos = AMBU_Solicitud_Baja.objects.filter(id=pk).values_list('sbja_activos')
        
        # SI EXISTEN ACTIVOS
        if (activos[0][0] != None and len(activos[0]) > 0):
            for ac in activos:
                
                #    SE OBTIENE EL ACTIVO
                activo = AMBU_Activo.objects.get(id=ac[0])
                
                #   SI LA SOLICITUD ES DE TRASPASO CAMBIA EL USUARIO RESPONSABLE
                if (query.sbja_solicitud_traspaso):
                    activo.act_usuario_responsabe = query.sbja_usuario_nuevo
                else:
                    activo.act_estatus = False
                activo.save()
        else:
            return Response("No se han encontrado activos en la solicitud", status=status.HTTP_400_BAD_REQUEST)   
        #   SE SALVA EL USUARIO
        query.save()
        return Response(status=status.HTTP_200_OK)
#   RECHAZA UNA SOLICITUD
class solicitudRechazar(generics.UpdateAPIView):
    
    def put(self, request, *args, **kwargs):
        
        #   OBTIENE LA PK DE LA RUTA
        pk = kwargs.get('pk') 

        #   CONSULTA
        query = AMBU_Solicitud_Baja.objects.get(id=pk)

        # SI EL QUERY NO TIENE DATOS RETORNA ERROR
        if query is None:
            return Response("No se ha encontrado la solicitud", status=status.HTTP_400_BAD_REQUEST)   

        #   CAMBIA EL ESTADO DE LA SOLICITUD
        query.sbja_estado_solicitud = "R"
        #   SE SALVA EL USUARIO
        query.save()
        return Response(status=status.HTTP_200_OK)