from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from Biblioteca_BackEnd.api.serializers.usuarioSerializer import (usuarioListSerializer,
    recoverySerializer,  
    customUserRegisterSerializer)
from Biblioteca_BackEnd.api.models import AMBU_CustomeUsuario
from django.db.models import Q
import json
from rest_framework import status

#   LISTA LOS USUAIRO
class usuarioLView (generics.ListAPIView):
    
    #   CONSULTA
    queryset = AMBU_CustomeUsuario.objects.filter(is_active=1)

    #   MAPEA LOS DATOS
    serializer_class = usuarioListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

#   OBTIENE O ACTUALIZA UN USUARIO
class usuarioRUView (generics.RetrieveUpdateAPIView):

    #   OBTIENE EL USUARIO
    lookup_field = 'pk'

    #   CONSULTA
    queryset = AMBU_CustomeUsuario.objects.all()

    #   MAPEA LOS DATOS
    serializer_class = usuarioListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

#   SE ENCARGA DE RECUPERAR Y CAMBIAR LA CONTRASEÑA
class recoveryCView (generics.CreateAPIView):

    def post(self, request, *args, **kwargs):

        #   OBTIENE LOS DATOS Y LOS MAPEA EN UN JSON
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        #   CONSULTA
        query = AMBU_CustomeUsuario.objects.filter(Q(email=body_data['email']) & Q(
            cus_identificacion=body_data['cus_identificacion']))
        
        #   REVISA SI ESTISTE UN USUARIO
        #   NOTA: DEVUELVE UNA TUPLA, POR ESO SE UTILIZAN INDICES
        if (len(query) > 0):
            #   SI LA CONSULTA TIENE UN TAMAÑO MAYOR A CERO ENTONES SI ENCONTRÓ AL USUAIRO
            #   CAMBIA LA CONTRASEÑA Y SALVA LOS DATOS
            query[0].set_password(body_data['password'])
            query[0].save()
            #   RETORNA QUE SE LOGRÓ CON ÉXITO
            serializer = recoverySerializer(query[0])
            return Response(status=status.HTTP_200_OK)
        else:
            #   RETORNA UN BAD_REQUEST SI NO ENCUENTRA AL USUAIRO
            return Response(status=status.HTTP_400_BAD_REQUEST)

#   REGISTRA UN USUARIO
class registerCView (generics.CreateAPIView):

    #   CONSULTA
    queryset = AMBU_CustomeUsuario.objects.all()

    #   MAPEA LOS DATOS
    serializer_class = customUserRegisterSerializer

class eliminarUsuario(generics.UpdateAPIView):
    
    def put(self, request, *args, **kwargs):
        
        #   OBTIENE LA PK DE LA RUTA
        pk = kwargs.get('pk') 

        #   CONSULTA
        query = AMBU_CustomeUsuario.objects.get(id=pk)

        # SI EL QUERY NO TIENE DATOS RETORNA ERROR
        if query is None:
            return Response("No se ha encontrado el usuario", status=status.HTTP_400_BAD_REQUEST)   

        #   CAMBIA EL ESTADO DEL USUARIO
        query.is_active = 0
        #   SE SALVA EL USUARIO
        query.save()
        return Response(status=status.HTTP_200_OK)