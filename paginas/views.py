from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name= 'index.html'

class DocesView(TemplateView):
    template_name= 'doces.html'

class MacaromView(TemplateView):
    template_name= 'macarons.html'

class BoloView(TemplateView):
    template_name= 'bolo.html'

    