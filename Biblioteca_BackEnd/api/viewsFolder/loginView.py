from django.shortcuts import render
from rest_framework import generics, mixins
from Biblioteca_BackEnd.api.serializers.loginSerializer import loginSerializer
from Biblioteca_BackEnd.api.serializers.usuarioSerializer import customSerializer
from Biblioteca_BackEnd.api.models import AMBU_Usuario, AMBU_CustomeUsuario
from rest_framework.response import Response
from django.db.models import Q
import json
from django.contrib.auth import authenticate, logout, login
from rest_framework.views import APIView

class loginCView (generics.CreateAPIView):
    queryset = AMBU_CustomeUsuario.objects.all()

    serializer_class = customSerializer

    def post(self, request, *args, **kwargs):

        email = kwargs.get('email')

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        query = AMBU_CustomeUsuario.objects.filter(
            username=body_data['username'])
        test = False
        user = authenticate(
            username=body_data['username'], password=body_data['password'])
        print(user)
        if user:
            login(request, user)
            ser = customSerializer(user, many=False)
        else:
            # print(query)
            ser = customSerializer(user, many=True)
        return Response(ser.data)


class logoutView (APIView):

     def post(self, request, format=None):
        # simply delete the token to force a login
        #request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# from django.shortcuts import render
# from rest_framework import generics, mixins
# from Biblioteca_BackEnd.api.serializers.loginSerializer import loginSerializer
# from Biblioteca_BackEnd.api.serializers.usuarioSerializer import usuarioListSerializer
# from Biblioteca_BackEnd.api.models import AMBU_Usuario
# from rest_framework.response import Response
# from django.db.models import Q
# import json


# class loginCView (generics.CreateAPIView):
#     queryset = AMBU_Usuario.objects.all()

#     serializer_class = usuarioListSerializer

#     def post(self, request, *args, **kwargs):
#         body_unicode = request.body.decode('utf-8')
#         body_data = json.loads(body_unicode)
#         query = AMBU_Usuario.objects.filter(Q(usu_clave=body_data['usu_clave']) & Q(
#             usu_identificacion=body_data['usu_identificacion']))
#         if len(query) > 0:
#             query = list(query)[0]
#             ser = usuarioListSerializer(query, many=False)
#         else:
#             ser = usuarioListSerializer(query, many=True)
#         return Response(ser.data)
