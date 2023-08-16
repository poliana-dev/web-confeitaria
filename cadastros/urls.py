from django.urls import path
from .views import BolosCreate,DocesCreate, MacaronsCreate, SaborCreate

urlpatterns = [
    path('cadastrar/bolos/', BolosCreate.as_view(), name='cadastrar-bolos'),
    path('cadastrar/doces/', DocesCreate.as_view(), name= 'cadastrar-doces'),
    path('cadastrar/macarons/', MacaronsCreate.as_view(), name= 'cadastrar-macarons'),
    path('cadastrar/sabor/', SaborCreate.as_view(), name= 'cadastrar-sabor'),
    
    
    
]