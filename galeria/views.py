#views

from django.shortcuts import render, redirect, get_object_or_404

from galeria.models import Post, Comentario

from galeria.forms import PostForms, ComentarioForm

from django.contrib import messages



def  index(request):
    return render(request, 'galeria/index.html')

def card(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    posts = Post.objects.filter(privacidade=True).order_by('-data_hora_criacao')
    context = {'posts': posts}
    return render(request, 'galeria/card.html', context)

def postar(request):

    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = PostForms
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            form.instance.autor = request.user
            form.save()
            messages.success(request, 'Nova post publicado com sucesso!')
            return redirect('card')

    return render(request,'galeria/pages/postar.html', {'form': form})

def editar_post(request):
    pass

def apagar_post(request):
    pass

def verpost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            novo_comentario = form.save(commit=False)
            novo_comentario.autor = request.user
            novo_comentario.post = post
            novo_comentario.save()
           
            return redirect('verpost', post_id=post_id)
    else:
        form = ComentarioForm()
    return render(request, 'galeria/pages/ver-post.html', {'post': post, 'form': form})

def perfil(request):
    return render(request, 'galeria/pages/perfil.html')

def amigos(request):
    return render(request, 'galeria/pages/amigos.html')
