from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.activoView import ActivoLCView, ActivoRUView, ActivoBySeccionLView
app_name = "api"
ACTIVO = 'activo/'
ACTIVOBYSECCION = 'activobyseccion/'
urlpatterns = [
    url(r'^'+ACTIVO+'$', ActivoLCView.as_view(), name="activo-lc"),
    url(r'^'+ACTIVO+'(?P<pk>\d+)$', ActivoRUView.as_view(), name="activo-ru"),
    url(r'^'+ACTIVOBYSECCION+'(?P<fk>\d+)$', ActivoBySeccionLView.as_view(), name="activobyseccion-l"),
]