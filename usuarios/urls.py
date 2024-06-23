from django.urls import path
from usuarios.views import login, cadastro, postar
urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('postar', postar, name='postar'),
]