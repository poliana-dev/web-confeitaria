from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Bolos, Doces, Macarons, Sabor

class BolosCreate(CreateView):
    model = Bolos
    fields= ['nome', 'descricao', 'tamanho','sabor', 'observacao',]
    template_name= 'formBolos.html'
    success_url = reverse_lazy=('bolos')

class DocesCreate(CreateView):
    model= Doces
    fields = ['nome','descricao', 'tamanho', 'sabor']
    template_name= 'formDoces.html'
    success_url= reverse_lazy=('doces')

class MacaronsCreate(CreateView):
    model=Macarons
    fields= ['nome','descricao', 'tamanho', 'sabor']
    template_name= 'formMacarons.html'
    success_url= reverse_lazy('macarons')

class SaborCreate(CreateView):
    model= Sabor
    fields= ['sabor']
    template_name= 'formSabor.html'
    success_url= reverse_lazy('inicio')


    


