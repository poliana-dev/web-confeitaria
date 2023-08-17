from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Bolos, Doces, Macarons, Sabor

class BolosCreate(CreateView):
    model = Bolos
    fields= ['nome', 'descricao', 'tamanho','sabor', 'observacao',]
    template_name= 'formBolos.html'
    success_url = reverse_lazy=('inicio')

class DocesCreate(CreateView):
    model= Doces
    fields = ['nome','descricao', 'tamanho', 'sabor']
    template_name= 'formDoces.html'
    success_url= reverse_lazy=('inicio')

class MacaronsCreate(CreateView):
    model=Macarons
    fields= ['nome','descricao', 'tamanho', 'sabor']
    template_name= 'formMacarons.html'
    success_url= reverse_lazy('inicio')

class SaborCreate(CreateView):
    model= Sabor
    fields= ['sabor']
    template_name= 'formSabor.html'
    success_url= reverse_lazy('inicio')

### UPDATE ###

class BolosUpdate(UpdateView):
    model= Bolos
    fields= ['nome', 'descricao', 'tamanho','sabor', 'observacao',]
    template_name= 'formBolos.html'
    success_url = reverse_lazy=('inicio')

class DocesUpdate(UpdateView):
    model= Doces
    fields = ['nome','descricao', 'tamanho', 'sabor']
    template_name= 'formDoces.html'
    success_url= reverse_lazy=('inicio')

class MacaronsUpdate(UpdateView):
    model=Macarons
    fields= ['nome','descricao', 'tamanho', 'sabor']
    template_name= 'formMacarons.html'
    success_url= reverse_lazy('inicio')

class SaborUpdate(UpdateView):
    model= Sabor
    fields= ['sabor']
    template_name= 'formSabor.html'
    success_url= reverse_lazy('inicio')

#### DELETE ####

class BolosDelete(DeleteView):
    model=Bolos
    template_name= 'deletar/form-excluir.html'
    success_url= reverse_lazy('inicio')

class DocesDelete(DeleteView):
    model=Doces
    template_name= 'deletar/form-excluir.html'
    success_url= reverse_lazy('inicio')

class MacaronsDelete(DeleteView):
    model= Macarons
    template_name= 'deletar/form-excluir.html'
    success_url= reverse_lazy('inicio')

class SaborDelete(DeleteView):
    model= Sabor
    template_name= 'deletar/form-excluir.html'
    success_url= reverse_lazy('inicio')

### LIST ###




    


