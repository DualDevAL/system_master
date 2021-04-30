from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
#from django.db.models.signals import post_save
#from django.utils.text import slugify
#from django.urls import reverse
from ckeditor.fields import RichTextField
#from django.utils.html import mark_safe
# Create your models here.


class GameCategory(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    servant = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Adicionar Gênero"
        verbose_name_plural = "Adicionar Gêneros"
        ordering = ["-servant"]

    def __str__(self):
        return self.name

class publisher(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    servant = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Adicionar Editora"
        verbose_name_plural = "Adicionar Editora"
        ordering = ["-servant"]

    def __str__(self):
        return self.name

class Operational_System(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    servant = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Adicionar Sistema Operacional"
        verbose_name_plural = "Adicionar Sistema Operacional"
        ordering = ["-servant"]

    def __str__(self):
        return self.name

class Select_Language(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    servant = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Adicionar Linguagem"
        verbose_name_plural = "Adicionar Linguagem"
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
    image = models.ImageField(upload_to='general_post', blank=True, null=True, verbose_name='Imagem')
    description = RichTextField(max_length=500, verbose_name='Descrição', null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)
    
    published = models.DateTimeField(default=now, null=True, verbose_name='Publicado')
    publisher = models.ManyToManyField(publisher, related_name="get_posts", verbose_name='Editora', null=True)
    Operational_System = models.ManyToManyField(Operational_System, related_name="get_posts", verbose_name='Sistema Operacional', null=True)
    servant = models.DateTimeField(auto_now_add=True)
    Changed = models.DateTimeField(auto_now=True)
    Select_Language = models.ManyToManyField(Select_Language, related_name="get_posts", verbose_name='Linguagens', null=True)
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor', null=True,)

    #def get_absolute_url(self):
    #    return reverse('home', args=[self.pk])

    class Meta:
        verbose_name = "Adicionar Jogo"
        verbose_name_plural = "Adicionar Jogos"

    def __str__(self):
        return str(self.title).capitalize()

