#views

from django.shortcuts import render

from galeria.models import Post


def  index(request):
    return render(request, 'galeria/index.html')

def cadastro(request):
    posts = Post.objects.filter(privacidade=True)
    context = {'posts': posts}
    return render(request, 'galeria/card.html', context)
