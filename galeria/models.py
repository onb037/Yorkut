from django.db import models


class Perfis(models.Model):
    usuario = models.OneToOneField('Usuarios', on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='perfil_fotos/', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f'Perfil [usuario={self.usuario.nomeUsuario}]'


class Amigos(models.Model):
    usuario = models.ForeignKey('Usuarios', related_name='amigos_usuario', on_delete=models.CASCADE)
    amigo = models.ForeignKey('Usuarios', related_name='amigos_amigo', on_delete=models.CASCADE)
    data_amizade = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'amigo')

    def __str__(self) -> str:
        return f'Amizade [usuario={self.usuario.nomeUsuario}, amigo={self.amigo.nomeUsuario}]'


class Postagens(models.Model):
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Postagem [usuario={self.usuario.nomeUsuario}, data_postagem={self.data_postagem}]'


class Comentarios(models.Model):
    postagem = models.ForeignKey('Postagens', related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Comentario [postagem={self.postagem.id}, usuario={self.usuario.nomeUsuario}]'


class Curtidas(models.Model):
    postagem = models.ForeignKey('Postagens', related_name='curtidas', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    data_curtida = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Curtida [postagem={self.postagem.id}, usuario={self.usuario.nomeUsuario}]'


class Notificacoes(models.Model):
    usuario = models.ForeignKey('Usuarios', related_name='notificacoes', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)  # Ex: 'amizade', 'curtida', 'comentario'
    mensagem = models.TextField()
    lida = models.BooleanField(default=False)
    data_notificacao = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Notificacao [usuario={self.usuario.nomeUsuario}, tipo={self.tipo}]'


class ConfiguracoesPrivacidade(models.Model):
    usuario = models.OneToOneField('Usuarios', on_delete=models.CASCADE)
    pode_ver_postagens = models.CharField(max_length=50, default='amigos')  # Ex: 'todos', 'amigos', 'ninguem'
    pode_ver_perfil = models.CharField(max_length=50, default='amigos')

    def __str__(self) -> str:
        return f'ConfiguracaoPrivacidade [usuario={self.usuario.nomeUsuario}]'
