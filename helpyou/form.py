from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import TB_participantes
from .models import TB_psicologos
from .models import TB_salas

class LoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)

class Cadastro_Participante(ModelForm):
    class Meta:
        model = TB_participantes
        fields = ['nome', 'cpf', 'email', 'senha', 'telefone', 'disturbio','sala_inserido']

class Cadastro_Psicologo(ModelForm):
    class Meta:
        model = TB_psicologos
        fields = ['nome', 'cpf', 'registro_crp', 'email', 'senha', 'telefone']

class Criar_Sala(ModelForm):
    class Meta:
        model = TB_salas
        fields = ['cod_sala', 'nome', 'admin', 'descricao', 'categoria']
