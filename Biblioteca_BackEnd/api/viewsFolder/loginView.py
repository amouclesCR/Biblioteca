from django.shortcuts import render
from rest_framework import generics, mixins
from Biblioteca_BackEnd.api.serializers.usuarioSerializer import customSerializer
from Biblioteca_BackEnd.api.models import AMBU_CustomeUsuario
from rest_framework.response import Response
from django.db.models import Q
import json
from django.contrib.auth import authenticate, logout, login
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
#   REVISA SI EL USUARIO EXISTE PARA REALIZAR EL LOGIN DEL MISMO
class loginCView (generics.CreateAPIView):

    #   QUERY DE LA CONSULTA
    queryset = AMBU_CustomeUsuario.objects.all()

    #   MAPEA LOS DATOS
    serializer_class = customSerializer

    #   FUNCIÓN POST
    def post(self, request, *args, **kwargs):

        #   OBTIENE LOS DATOS ENVIADOS EN EL POST
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        #   QUERY PARA FILTRAR LOS DATOS
        query = AMBU_CustomeUsuario.objects.filter(
            username=body_data['username'])
        
        #   AUTENTICACIÓN DEL DEL USUARIO
        user = authenticate(
            username=body_data['username'], password=body_data['password'])
        
        if user:
            login(request, user)
            #refresh = RefreshToken.for_user(user)
            ser = customSerializer(user, many=False)
        else:
            ser = customSerializer(user, many=True)
        return Response(ser.data)

#   REALIZA EL LOGOUT DEL USUARIO
class logoutView (APIView):

     def post(self, request, format=None):
       
        return Response(status=status.HTTP_200_OK)
