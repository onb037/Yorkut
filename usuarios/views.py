from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from usuarios.forms import LoginForms, CadastroForms, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.exceptions import MultipleObjectsReturned
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect

import logging

logger = logging.getLogger(__name__)

@csrf_protect
def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome_login']
            senha = form.cleaned_data['senha']

            usuario = auth.authenticate(request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso!")
                logger.info(f"Usuário {nome} logado com sucesso.")
                return redirect('card')
            else:
                messages.error(request, "Erro ao efetuar login!")
                logger.warning(f"Tentativa de login falha para o usuário {nome}.")
                return redirect('login')
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome_cadastro']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha_1']

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existente!")
                return redirect('cadastro')

            try:
                usuario = User.objects.create_user(username=nome, email=email, password=senha)
                usuario.save()
                messages.success(request, "Cadastrado com sucesso!")
                logger.info(f"Novo usuário cadastrado: {nome}")
                return redirect('login')
            except Exception as e:
                messages.error(request, f"Ocorreu um erro durante o cadastro: {e}")
                logger.error(f"Erro ao cadastrar usuário {nome}: {e}")

    return render(request, 'usuarios/cadastro.html', {'form': form})

def redefinir(request):
    return render(request, 'usuarios/redefinir-senha.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Deslogado com sucesso!")
    logger.info(f"Usuário deslogado.")
    return redirect('login')

@csrf_protect
def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                new_password = get_random_string(12)
                user.set_password(new_password)
                user.save()

                send_mail(
                    'Redefinição de senha',
                    f'Sua nova senha é: {new_password}',
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request, "Senha alterada com sucesso!")
                logger.info(f"Senha redefinida para o usuário com email: {email}")
                return HttpResponseRedirect(reverse('login'))
            except User.DoesNotExist:
                form.add_error('email', 'Nenhum usuário encontrado com este e-mail.')
                logger.error(f"Tentativa de redefinição de senha falhou. Nenhum usuário encontrado com o email: {email}")
            except MultipleObjectsReturned:
                form.add_error('email', 'Há mais de um usuário com este e-mail. Entre em contato com o suporte.')
                logger.error(f"Tentativa de redefinição de senha falhou. Múltiplos usuários com o email: {email}")
    else:
        form = PasswordResetForm()
    return render(request, 'usuarios/reset_password.html', {'form': form})

