from django.urls import path
from usuarios.views import login, cadastro, logout, reset_password
urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('reset_password', reset_password, name='reset_password'),
    path('logout', logout, name='logout')
]