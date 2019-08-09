from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.rolView import rolLCView
app_name = "api"
ROL = 'rol/'
urlpatterns = [
    url(r'^'+ROL+'$', rolLCView.as_view(), name="rol-l"),   
]