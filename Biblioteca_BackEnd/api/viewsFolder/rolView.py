from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, mixins
from Biblioteca_BackEnd.api.serializers.rolSerializar import rolSerializer
from Biblioteca_BackEnd.api.models import AMBU_Rol

class rolLCView (generics.ListAPIView):
    queryset = AMBU_Rol.objects.all()
    
    serializer_class = rolSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)