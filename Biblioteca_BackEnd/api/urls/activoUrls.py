from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.activoView import ActivoLCView, ActivoRUView
app_name = "api"
ACTIVO = 'activo/'
urlpatterns = [
    url(r'^'+ACTIVO+'$', ActivoLCView.as_view(), name="activo-lc"),
    url(r'^'+ACTIVO+'(?P<pk>\d+)$', ActivoRUView.as_view(), name="activo-ru"),
]