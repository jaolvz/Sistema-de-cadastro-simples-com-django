from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User


class Perfil (models.Model):
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/',null=True, blank=True)
    foto_capa = models.ImageField(upload_to='fotos_capa/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    

    @classmethod
    def url_foto_perfil(cls,user):
        perfil = cls.objects.filter(Usuario=user).first()
        if perfil and perfil.foto_perfil:
            return perfil.foto_perfil.url
        return None
    
    @classmethod
    def url_foto_capa(cls,user):
        perfil = cls.objects.filter(Usuario=user).first()
        if perfil and perfil.foto_capa:
            return perfil.foto_capa.url
        return None


class Post (models.Model):


    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    conteudo = models.TextField()
    postado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Postado por {self.autor.username}'
    
    @classmethod
    def retornar_posts_por_usuario(cls,user):
        return cls.objects.filter(autor=user).order_by('-postado')
    
class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    conteudo = models.TextField()
    postado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comentario de {sef.autor.username}'
    

    
