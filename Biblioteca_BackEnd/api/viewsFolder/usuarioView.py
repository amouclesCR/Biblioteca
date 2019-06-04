from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from Biblioteca_BackEnd.api.serializers.usuarioSerializer import usuarioListSerializer, usuarioUpdateSerializer, usuarioCreateSerializer, recoverySerializer, customSerializer, customUserRegisterSerializer
from Biblioteca_BackEnd.api.models import AMBU_Usuario, AMBU_CustomeUsuario
from django.db.models import Q
import json


class usuarioLCView (generics.ListCreateAPIView):
    queryset = AMBU_CustomeUsuario.objects.all()

    serializer_class = usuarioListSerializer

    def get_serializer_class(self):
        method = self.request.method
        if method == 'POST':
            return usuarioCreateSerializer
        else:
            return usuarioListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class usuarioRUView (generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'

    queryset = AMBU_CustomeUsuario.objects.all()

    serializer_class = usuarioListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class recoveryCView (generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        query = AMBU_Usuario.objects.filter(Q(id=pk) & Q(usu_correo=body_data['usu_correo']) & Q(
            usu_identificacion=body_data['usu_identificacion']))
        print(query)
        if (len(query) > 0):
            query[0].usu_clave = body_data['usu_clave']
            query[0].save()
            serializer = recoverySerializer(query[0])
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class customeCView (generics.CreateAPIView):
    queryset = AMBU_CustomeUsuario.objects.all()

    serializer_class = customUserRegisterSerializer
