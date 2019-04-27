from django.conf.urls import url
from Biblioteca_BackEnd.api.viewsFolder.loginView import loginCView
app_name = "api"
LOGIN = 'login/'
urlpatterns = [
    url(r'^'+LOGIN+'$', loginCView.as_view(), name="login-post"),   
]