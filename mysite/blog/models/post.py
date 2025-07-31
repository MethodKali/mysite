from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) #Titulo do Post
    slug = models.SlugField(max_length=200, unique=True) #Indentificação do Post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') #Autor do Post
    updated_on = models.DateTimeField(auto_now=True) #Data de atualização do Post
    content = models.TextField() #Texto do Post
    created_on = models.DateTimeField(auto_now_add=True) #Data de criação do Post
    status = models.IntegerField(choices=STATUS, default=0) #Criação de um rascunho ou publicação do Post

    class Meta:
        ordering = ['-created_on'] #Ordenar os posts pela data de criação

    def __str__(self): #Função para retornar os titulos dos posts criados
        return self.title