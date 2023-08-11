from django.urls import path
from .views import IndexView, DocesView
from .views import MacaromView, BoloView

urlpatterns=[
    path('', IndexView.as_view(), name='inicio'),
    path('doces/', DocesView.as_view(), name='doces'),
    path('bolos/', BoloView.as_view(), name='bolos'),
    path('macarons/', MacaromView.as_view(), name='macarons'),

]