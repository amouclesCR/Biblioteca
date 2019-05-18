from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.activoView import ActivoLCView, ActivoRUView, ActivoBySeccionLView, ActivoByUsuarioLView, ActivoByNumeroActivoLView
app_name = "api"
ACTIVO = 'activo/'
ACTIVOBYSECCION = 'activobyseccion/'
ACTIVOBYUSUARIO = 'activobyusuario/'
ACTIVOBYNUMEROACTIVO = 'activobynumeroactivo/'
urlpatterns = [
    url(r'^'+ACTIVO+'$', ActivoLCView.as_view(), name="activo-lc"),
    url(r'^'+ACTIVO+'(?P<pk>\d+)$', ActivoRUView.as_view(), name="activo-ru"),
    url(r'^'+ACTIVOBYSECCION+'(?P<fk>\d+)$', ActivoBySeccionLView.as_view(), name="activobyseccion-l"),
    url(r'^'+ACTIVOBYUSUARIO+'(?P<fk>\d+)$', ActivoByUsuarioLView.as_view(), name="activobyusuario-l"),
    url(r'^'+ACTIVOBYNUMEROACTIVO+'(?P<numeroactivo>[a-zA-Z0-9]+)$', ActivoByNumeroActivoLView.as_view(), name="activobynumeroactivo-l"),
]