from django.urls import path
from .views import *

urlpatterns = [
    path('js/criar', bolo_create, name='js-criar'),

    path('cadastrar/bolos/', BolosCreate.as_view(), name='cadastrar-bolos'),
    path('cadastrar/doces/', DocesCreate.as_view(), name= 'cadastrar-doces'),
    path('cadastrar/macarons/', MacaronsCreate.as_view(), name= 'cadastrar-macarons'),
    path('cadastrar/sabor/', SaborCreate.as_view(), name= 'cadastrar-sabor'),

    path('excluir/bolos/<int:pk>/', BolosDelete.as_view(), name='excluir-bolos'),
    path('excluir/doces/<int:pk>/', DocesDelete.as_view(), name='excluir-doces'),
    path('excluir/macarons/<int:pk>/', MacaronsDelete.as_view(), name='excluir-macarons'),
    path('excluir/sabores/<int:pk>/', SaborDelete.as_view(), name='excluir-sabor'),

    path('listar', BolosList.as_view(), name='listar-bolos')

    
    
    
]