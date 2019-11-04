"""meu_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
