from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.solicitudBajaView import solicitudBajaLCView, solicitudBajaRUView, solicitudByUsuarioL, solicitudAprobar, solicitudBajaLView
app_name = "api"
SOLICITUD = 'solicitud/'
SOLICITUDBYUSUARIO = 'solicitudbyusuario/'
SOLICITUDAPROBAR = 'solicitudaprobar/'
SOLICITUDNOAPROBADAS = 'solicitudnoaprobar/'
urlpatterns = [
    url(r'^'+SOLICITUD+'$', solicitudBajaLCView.as_view(), name="solicitud-lc"),
    url(r'^'+SOLICITUD+'(?P<pk>\d+)$', solicitudBajaRUView.as_view(), name="solicitud-ru"),
    url(r'^'+SOLICITUDNOAPROBADAS+'$', solicitudBajaLView.as_view(), name="solicitud-l"),
    url(r'^'+SOLICITUDAPROBAR+'(?P<pk>\d+)$', solicitudAprobar.as_view(), name="solicitud-u"),
    url(r'^'+SOLICITUDBYUSUARIO+'(?P<pk>\d+)$', solicitudByUsuarioL.as_view(), name="solicitudbyusuario-l"),
]