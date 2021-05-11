from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
#from django.db.models.signals import post_save
#from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
#from django.utils.html import mark_safe
# Create your models here.


class GameCategory(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Adicionar Gênero"
        verbose_name_plural = "Adicionar Gêneros"
        ordering = ["-create"]

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Adicionar Editora"
        verbose_name_plural = "Adicionar Editora"
        ordering = ["-create"]

    def __str__(self):
        return self.name


class Age_Range(models.Model):
    age = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Faixa Etária"
        verbose_name_plural = "Faixa Etária"
        ordering = ["-create"]

    def __str__(self):
        return self.age


class Operational_System(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Adicionar Sistema Operacional"
        verbose_name_plural = "Adicionar Sistema Operacional"
        ordering = ["-create"]

    def __str__(self):
        return self.name



class Graphics_Engine(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Motor Gráfico"
        verbose_name_plural = "Motor Gráfico"
        ordering = ["-create"]

    def __str__(self):
        return self.name


class Designer(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "designer"
        verbose_name_plural = "designer"
        ordering = ["-create"]

    def __str__(self):
        return self.name


class Select_Language(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Adicionar Linguagem"
        verbose_name_plural = "Adicionar Linguagem"
        ordering = ["-create"]

    def __str__(self):
        return self.name



class MinimumRequirements(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Requisitos Minimos"
        verbose_name_plural = "Requisitos Minimos"
        ordering = ["-create"]

    def __str__(self):
        return self.name



class RecommendedRequirements(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Requisitos Recomendados"
        verbose_name_plural = "Requisitos Recomendados"
        ordering = ["-create"]

    def __str__(self):
        return self.name



class Player(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=now)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Número de Jogadores"
        verbose_name_plural = "Adicionar Linguagem"
        ordering = ["-create"]

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

    genre = models.ManyToManyField(GameCategory, related_name="get_posts", verbose_name='Gênero', blank=True, null=True)
    image = models.ImageField(upload_to='general_post', blank=True, null=True, verbose_name='Imagem')
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)
    
    published = models.DateTimeField(default=now, null=True, verbose_name='Publicado' ,blank=True)
    publisher = models.ManyToManyField(Publisher, related_name="get_posts", verbose_name='Editora', blank=True, null=True)
    Operational_System = models.ManyToManyField(Operational_System, related_name="get_posts", verbose_name='Sistema Operacional', blank=True, null=True)
    servant = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    Changed = models.DateTimeField(auto_now=True, blank=True, null=True)
    Select_Language = models.ManyToManyField(Select_Language, related_name="get_posts", verbose_name='Linguagens', blank=True, null=True)
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor', null=True)
    age_range = models.ManyToManyField(Age_Range, related_name="get_posts", verbose_name='Faixa Etária', blank=True, null=True)
    graphics_engine =  models.ManyToManyField(Graphics_Engine, related_name="get_posts", verbose_name='Motor Gráfico', blank=True, null=True)
    designer = models.ManyToManyField(Designer, related_name="get_posts", verbose_name='Projetista', blank=True, null=True)
    player = models.ManyToManyField(Player, related_name="get_posts", verbose_name='Número de Jogadores', blank=True, null=True)
    minimum_requirements = models.ManyToManyField(MinimumRequirements, related_name="get_posts", verbose_name='Requisitos Minimos', blank=True, null=True)
    recommended_requirements = models.ManyToManyField(RecommendedRequirements, related_name="get_posts", verbose_name='Requisitos Recomendados', blank=True, null=True)
   

    def get_absolute_url_update(self):
            return reverse("post_new", args=[self.slug])
    class Meta:
        verbose_name = "Adicionar Jogo"
        verbose_name_plural = "Adicionar Jogos"

    def __str__(self):
        return str(self.title).capitalize()

