# versao django
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Bolos, Doces, Macarons, Sabor

# versao ajax
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import *

# CRUD AJAX

def bolo_create(request):
    form= boloForm()
    context= {'form' : form}
    html_form = render_to_string('create-parcial/create-bolo.html', context, request=request)
    return JsonResponse({'html_form': html_form})






# CRUD DJANGO

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

class BolosList(ListView):
    model= Bolos
    template_name= 'listas/form-listarBolos.html'

class DocesList(ListView):
    model = Doces
    template_name = 'listas/form-listarDoces'

class MacaronsList(ListView):
    model = Macarons
    template_name = 'listas/form-listarMacarons'

class SaborList(ListView):
    model = Sabor
    template_name = 'listas/form-listarSabor'


    


