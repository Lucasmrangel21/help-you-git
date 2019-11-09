from django.urls import path, re_path
from helpyou.views import index, room
from django.contrib import admin

app_name = 'helpyou'

urlpatterns = [
    path('index/', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]
