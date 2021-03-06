from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.usuarioView import (usuarioLView, 
    usuarioRUView, 
    recoveryCView, 
    registerCView,
    eliminarUsuario)
from Biblioteca_BackEnd.api.viewsFolder.loginView import loginCView
app_name = "api"
USUARIO = 'usuario/'
RECOVERY = 'recovery/'
REGISTER = 'register/'
ELIMINAR = 'eliminar/'
urlpatterns = [
    url(r'^'+USUARIO+'$', usuarioLView.as_view(), name="usuario-lc"),
    url(r'^'+REGISTER+'$', registerCView.as_view(), name="usuario-lc"),
    url(r'^'+USUARIO+'(?P<pk>\d+)$', usuarioRUView.as_view(), name="usuario-ru"),
    url(r'^'+USUARIO+ELIMINAR+'(?P<pk>\d+)$', eliminarUsuario.as_view(), name="usuario-ru"),
    url(r'^'+RECOVERY+'$', recoveryCView.as_view(), name="recovery-c"),
   
]