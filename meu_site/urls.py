from django.contrib import admin
from django.urls import path, include, re_path
from helpyou.views import home, user_login, novo_cadastro1, listagem_salas, novo_cadastro2, index, room



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('login/', user_login, name='url_login'),
    path('insert_participante/', novo_cadastro1, name='url_insert_participante'),
    path('listagem_salas/', listagem_salas, name='url_listagem_salas'),
    path('salas_sugeridas/', novo_cadastro2, name='url_salas_sugeridas'),
    path('index/', index, name='index'),
    path('chat/', include('helpyou.urls', namespace='chat')),

]
