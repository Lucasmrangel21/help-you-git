from django.contrib import admin
from django.urls import path, include, re_path
from helpyou.views import home, user_login, novo_cadastro1, listagem_salas, novo_cadastro2, \
    novo_psicologo, index, room, nova_sala, salas_sugeridas, informacao_sala



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('login/', user_login, name='url_login'),
    path('insert_participante/', novo_cadastro1, name='url_insert_participante'),
    path('insert_psicologo/', novo_psicologo, name='url_insert_psicologo'),
    path('listagem_salas', listagem_salas, name='url_listagem'),
    path('salas_sugeridas/', novo_cadastro2, name='url_salas_sugeridas'),
    path('index/', index, name='index'),
    path('chat/', include('helpyou.urls', namespace='chat')),
    path('insert_sala/', nova_sala, name='url_insert_sala'),
    path('salas_sugerida/', salas_sugeridas),
    path('descricao_sala/', informacao_sala, name='url_descricao'),

]
