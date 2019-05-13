"""Biblioteca_BackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Biblioteca_BackEnd.api.urls.seccionUrls', namespace='api-seccion')),
    path('api/', include('Biblioteca_BackEnd.api.urls.usuarioUrls', namespace='api-usuario')),
    path('api/', include('Biblioteca_BackEnd.api.urls.solicitudBajaUrls', namespace='api-solicitud')),
    path('api/', include('Biblioteca_BackEnd.api.urls.activoUrls', namespace='api-activo')),
    path('api/', include('Biblioteca_BackEnd.api.urls.bajaUrls', namespace='api-baja')),
    path('api/', include('Biblioteca_BackEnd.api.urls.loginUrls', namespace='api-login')),
    path('api/', include('Biblioteca_BackEnd.api.urls.departamentoUrls', namespace='api-departamento')),
    path('api/', include('Biblioteca_BackEnd.api.urls.rolUrls', namespace='api-rol'))
]
