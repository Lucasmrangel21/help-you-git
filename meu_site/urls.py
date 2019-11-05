from django.contrib import admin
from django.urls import path
from helpyou.views import home, user_login, novo_cadastro1, home2, listagem_salas, novo_cadastro2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('login/', user_login, name='url_login'),
    path('insert_participante/', novo_cadastro1, name='url_insert_participante'),
    path('home2/', home2, name='url_home2'),
    path('listagem_salas/', listagem_salas, name='url_listagem_salas'),
    path('insert_psicologo/', novo_cadastro2, name='url_insert_psicologo'),

]
