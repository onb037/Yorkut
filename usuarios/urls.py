from django.urls import path
from usuarios.views import login, cadastro, postar, logout, redefinir
urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('postar', postar, name='postar'),
    path('redefinir', redefinir, name='redefinir'),
    path('logout', logout, name='logout')
]