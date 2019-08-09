from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.bajaView import BajaLCView, BajaRUView
app_name = "api"
BAJA = 'baja/'
urlpatterns = [
    url(r'^'+BAJA+'$', BajaLCView.as_view(), name="baja-lc"),
    url(r'^'+BAJA+'(?P<pk>\d+)$', BajaRUView.as_view(), name="baja-ru"),
]