from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .form import LoginForm
from .models import TB_salas
from .form import Cadastro_Participante
from .form import Cadastro_Psicologo
from .form import Criar_Sala
from django.utils.safestring import mark_safe
import json

def home(request):
    return render(request, 'helpyou/home.html')

def listagem_salas(request):
    data = {}
    data['salas'] = TB_salas.objects.all()
    return render(request, 'helpyou/listagem_salas.html', data)

def salas_sugeridas(request):
    data = {}
    data['salas'] = TB_salas.objects.all()
    return redirect('helpyou/salas_sugeridas.html')

def novo_cadastro1(request):
    data = {}
    form = Cadastro_Participante(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('helpyou/listagem_salas')
    data['form'] = form
    return render(request, 'helpyou/insert_participante.html', data)

def novo_cadastro2(request):
    data = {}
    data['salas'] = TB_salas.objects.all()
    return render(request, 'helpyou/salas_sugeridas.html', data)

def novo_psicologo(request):
    data = {}
    form = Cadastro_Psicologo(request.POST or None)
    data['form'] = form
    return render(request, 'helpyou/insert_psicologo.html', data)

def nova_sala(request):
    data = {}
    form = Criar_Sala(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    data['form'] = form
    return render(request, 'helpyou/insert_sala.html', data)

def informacao_sala(request,pk):
    data = {}
    sala = TB_salas.objects.get(pk=pk)
    form = Criar_Sala(request.POST or None, instance=sala)
    if form.is_valid():
        form.save()
        return redirect('index')
    data['form'] = form
    data['sala'] = sala
    return render(request, 'helpyou/descricao_sala.html', data)



def index(request):
    return render(request, 'helpyou/index.html', {})

def room(request, room_name):
    return render(request, 'helpyou/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['guga@exemplo.com'],
                   senha=cd['senha'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'helpyou/login.html', {'form': form})