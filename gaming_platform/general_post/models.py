from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class GameCategory(models.Model):# nova função mais recente teve que fazer a instalção de bliblioteca pipenv install pillow
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    servant = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Adicionar Gênero"
        verbose_name_plural = "Adicionar Gêneros"
        ordering = ["-servant"]

    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS = (
        ('disponivel', 'Disponivel'),
        ('indisponivel', 'Indisponivel')

    )

    title = models.CharField(max_length=200, verbose_name='Título do jogo',  null=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)

    genre = models.ManyToManyField(GameCategory, related_name="get_posts", verbose_name='Gênero', null=True)
    image = models.ImageField(upload_to = 'general_post', null=True, verbose_name='Imagem')
    description = RichTextField(max_length=500, verbose_name='Descrição', null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='disponível',  null=True)

    published = models.DateTimeField(default=now, null=True, verbose_name='Publicado')
    servant = models.DateTimeField(auto_now_add=True)
    Changed = models.DateTimeField(auto_now=True)

    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor', null=True,)

    class Meta:
        verbose_name = "Adicionar Jogo"
        verbose_name_plural = "Adicionar Jogos"

    def __str__(self):
        return str(self.title).capitalize()

    

'''@receiver(template, sender=Post)
def insert_slug(sender, instance, **kwargs):
    if kwargs.get('created', False):
        print('Criando slug')
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save
'''
