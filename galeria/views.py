from django.shortcuts import render

from galeria.models import Post


def  index(request):
    
    return render(request, 'galeria/index.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'galeria/card.html', {"postagem": posts})
    

# Create your views here.
