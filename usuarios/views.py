from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

from .forms import PasswordResetForm

from django.core.exceptions import MultipleObjectsReturned

from django.utils.crypto import get_random_string

from django.core.mail import send_mail

def login(request):
        form = LoginForms()

        if request.method == 'POST':
            form = LoginForms(request.POST)

            if form.is_valid():
                 nome = form['nome_login'].value()
                 senha = form['senha'].value()

            usuario = auth.authenticate(
                 request,
                 username=nome,
                 password=senha
            )
            if usuario is not None:
                 auth.login(request, usuario)
                 messages.success(request, f"{nome} Logado com sucesso!")
                 return redirect('card')
            else:
                 messages.error(request, f"{nome} Erro ao efetuar login!")
                 return redirect('login')


        return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, "As senhas nao coincidem!")
                return redirect ('cadastro')
        
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuario ja existente!")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastrado com sucesso!")
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def redefinir(request):
     return render(request,'usuarios/redefinir-senha.html')
         
def logout(request):
     auth.logout(request)
     messages.success(request, "Deslogado com sucesso!")
     return redirect('login')

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                new_password = get_random_string(8)
                user.set_password(new_password)
                user.save()

                send_mail(
                    'Redefinição de senha',
                    f'Sua nova senha é: {new_password}',
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request, f"Senha alterada com sucesso!")
                return HttpResponseRedirect(reverse('login'))
            except User.DoesNotExist:
                form.add_error('email', 'Nenhum usuário encontrado com este e-mail.')
            except User.MultipleObjectsReturned:
                form.add_error('email', 'Há mais de um usuário com este e-mail. Entre em contato com o suporte.')
    else:
        form = PasswordResetForm()

    return render(request, 'usuarios/reset_password.html', {'form': form})

