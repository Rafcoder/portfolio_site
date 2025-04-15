from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('servicos/', views.servicos, name='servicos'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('projetos/', views.projetos, name='projetos'),
    path('contato/', views.contato, name='contato'),
]
