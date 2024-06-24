from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='perfis', blank=True)
    nome_usuario = models.CharField(max_length=255, blank=True)
    imagem = models.ImageField(upload_to='postagens', blank=True)
    legenda = models.TextField()
    data_hora_criacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.IntegerField(default=0)