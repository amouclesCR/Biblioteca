from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.usuarioView import usuarioLCView, usuarioRUView, recoveryCView, customeCView
from Biblioteca_BackEnd.api.viewsFolder.loginView import loginCView
app_name = "api"
USUARIO = 'usuario/'
RECOVERY = 'recovery/'
REGISTER = 'register/'
urlpatterns = [
    url(r'^'+USUARIO+'$', usuarioLCView.as_view(), name="usuario-lc"),
    url(r'^'+REGISTER+'$', customeCView.as_view(), name="usuario-lc"),
    url(r'^'+USUARIO+'(?P<pk>\d+)$', usuarioRUView.as_view(), name="usuario-ru"),
    url(r'^'+RECOVERY+'(?P<pk>\d+)$', recoveryCView.as_view(), name="recovery-c"),
   
]