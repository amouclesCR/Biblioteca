from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.solicitudBajaView import solicitudRechazar, solicitudBajaLCView, solicitudBajaRUView, solicitudByUsuarioL, solicitudAprobar, solicitudBajaLView
app_name = "api"
SOLICITUD = 'solicitud/'
SOLICITUDBYUSUARIO = 'solicitudbyusuario/'
SOLICITUDAPROBAR = 'solicitudaprobar/'
SOLICITUDNOAPROBADAS = 'solicitudnoaprobadas/'
SOLICITUDRECHAZAR = 'solicitudrechazar/'
urlpatterns = [
    url(r'^'+SOLICITUD+'$', solicitudBajaLCView.as_view(), name="solicitud-lc"),
    url(r'^'+SOLICITUD+'(?P<pk>\d+)$', solicitudBajaRUView.as_view(), name="solicitud-ru"),
    url(r'^'+SOLICITUD+SOLICITUDNOAPROBADAS+'$', solicitudBajaLView.as_view(), name="solicitud-l"),
    url(r'^'+SOLICITUD+SOLICITUDAPROBAR+'(?P<pk>\d+)$', solicitudAprobar.as_view(), name="solicitud-u"),
    url(r'^'+SOLICITUD+SOLICITUDBYUSUARIO+'(?P<pk>\d+)$', solicitudByUsuarioL.as_view(), name="solicitudbyusuario-l"),
    url(r'^'+SOLICITUD+SOLICITUDRECHAZAR+'(?P<pk>\d+)$', solicitudRechazar.as_view(), name="solicitudbyusuario-l"),
]