from django.shortcuts import render
from django.contrid.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class register(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='account/register.html'
# Create your views here.
