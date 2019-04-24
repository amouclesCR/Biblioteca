from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.usuarioView import usuarioLCView, usuarioRUView
app_name = "api"
USUARIO = 'usuario/'
urlpatterns = [
    url(r'^'+USUARIO+'$', usuarioLCView.as_view(), name="usuario-lc"),
    url(r'^'+USUARIO+'(?P<pk>\d+)$', usuarioRUView.as_view(), name="movies-ru"),
]