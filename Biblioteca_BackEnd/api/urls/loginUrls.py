from django.conf.urls import url
from django.urls import include
from Biblioteca_BackEnd.api.viewsFolder.loginView import loginCView, logoutView
app_name = "api"
LOGIN = 'login/'
LOGOUT = 'logout/'
urlpatterns = [
    url(r'^'+LOGIN+'$', loginCView.as_view(), name="login-post"),   
    url(r'^'+LOGOUT+'$', logoutView.as_view(), name="login-post"),   
]
# url_patterns = [
#     ...
#     # Can login by using /auth/login
#     url(r'^auth/', include('timed_auth_token.urls', namespace='auth')),
# ]