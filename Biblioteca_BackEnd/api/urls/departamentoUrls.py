from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.departamentoView import departamentoLCView, departamentoRUView
app_name = "api"
DEPARTAMENTO = 'departamento/'
urlpatterns = [
    url(r'^'+DEPARTAMENTO+'$', departamentoLCView.as_view(), name="ubicacion-lc"),
    url(r'^'+DEPARTAMENTO+'(?P<pk>\d+)$', departamentoRUView.as_view(), name="ubicacion-ru"),
]