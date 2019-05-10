from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.solicitudBajaView import solicitudBajaLCView, solicitudBajaRUView, solicitudByUsuarioL
app_name = "api"
SOLICITUD = 'solicitud/'
SOLICITUDBYUSUARIO = 'solicitudbyusuario/'
urlpatterns = [
    url(r'^'+SOLICITUD+'$', solicitudBajaLCView.as_view(), name="solicitud-lc"),
    url(r'^'+SOLICITUD+'(?P<pk>\d+)$', solicitudBajaRUView.as_view(), name="solicitud-ru"),
    url(r'^'+SOLICITUDBYUSUARIO+'(?P<pk>\d+)$', solicitudByUsuarioL.as_view(), name="solicitudbyusuario-l"),
]