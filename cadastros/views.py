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
    # realizar um post
    data= dict() # um dicionario que é equivalente uma lista
    if(request.method== 'POST'):  # se a solicitação for um post
        form= boloForm(request.POST) # retorna o formulario predefinido anteriormente 
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True # se for valido salve no dicionario
            bolos = Bolos.objects.all() # pega todos os objetos presentes em bolos
            data['html_list'] = render_to_string('create-parcial/parcial-list-bolo.html', {'object_list': bolos}) # adicionamos uma nova chave em data que armazenará os objetos 
        else:
            data['form_is_valid'] = False
    else:
        form= boloForm() # retorna apenas o formulario

    # encaminha uma resposta HTTP valida
    context= {'form' : form}
    data['html_form'] = render_to_string('create-parcial/create-bolo.html', context, request=request)
    return JsonResponse(data)






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
    success_url= reverse_lazy('listar-bolos')

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
    template_name= 'listas/listarBolo.html'

class DocesList(ListView):
    model = Doces
    template_name = 'listas/form-listarDoces'

class MacaronsList(ListView):
    model = Macarons
    template_name = 'listas/form-listarMacarons'

class SaborList(ListView):
    model = Sabor
    template_name = 'listas/form-listarSabor'


    


