from django.urls import path
from usuarios.views import login, cadastro, postar, logout
urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('postar', postar, name='postar'),
    path('logout', logout, name='logout')
]