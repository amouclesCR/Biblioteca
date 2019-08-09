from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.seccionView import SeccionLCView, SeccionRUView
app_name = "api"
SECCION = 'seccion/'
urlpatterns = [
    url(r'^'+SECCION+'$', SeccionLCView.as_view(), name="movies-list"),
    url(r'^'+SECCION+'(?P<pk>\d+)$', SeccionRUView.as_view(), name="movies-rud"),
]