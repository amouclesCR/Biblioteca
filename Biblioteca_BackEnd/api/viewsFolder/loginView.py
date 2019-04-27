from django.shortcuts import render
from rest_framework import generics, mixins
from Biblioteca_BackEnd.api.serializers.loginSerializer import loginSerializer
from Biblioteca_BackEnd.api.models import AMBU_Usuario
from rest_framework.response import Response
import json
class loginCView (generics.CreateAPIView):
    queryset = AMBU_Usuario.objects.all()
    
    serializer_class = loginSerializer
    
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        query = AMBU_Usuario.objects.filter(usu_clave=body_data['usu_clave'])
        ser = loginSerializer(query, many=True)
        return Response(ser.data)