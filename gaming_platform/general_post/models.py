from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.dispatch import receiver
#from django.utils.html import mark_safe
# Create your models here.


class GameCategory(models.Model):
    STATUS = (
        ('disponivel', 'Disponivel'),
        ('indisponivel', 'Indisponivel')
    ) 

    name = models.CharField(max_length=100, verbose_name='Categoria')
    published = models.DateTimeField(default=now, verbose_name='Publicado')
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)

    def get_absolute_url_update3(self):
        return reverse('category_edit', args=[self.pk])

    class Meta:
        verbose_name = "Adicionar Gênero"
        verbose_name_plural = "Adicionar Gêneros"
        ordering = ["-create"]

    def __str__(self):
        return self.name


class Publisher(models.Model):
    STATUS = (
        ('disponivel', 'Disponivel'),
        ('indisponivel', 'Indisponivel')
    ) 

    name = models.CharField(max_length=100, verbose_name='Editora')
    published = models.DateTimeField(default=now, verbose_name='Publicado')
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)

    def get_absolute_url_update4(self):
        return reverse('publisher_edit', args=[self.pk])

    class Meta:
        verbose_name = "Adicionar Editora"
        verbose_name_plural = "Adicionar Editora"
        ordering = ["-create"]

    def __str__(self):
        return self.name


class Age_Range(models.Model):
    STATUS = (
        ('disponivel', 'Disponivel'),
        ('indisponivel', 'Indisponivel')
    ) 

    age = models.CharField(max_length=100, verbose_name='Idade')
    published = models.DateTimeField(default=now, verbose_name='Publicado')
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)

    def get_absolute_url_update2(self):
        return reverse('age_edit', args=[self.pk])

    class Meta:
        verbose_name = "Faixa Etária"
        verbose_name_plural = "Faixa Etária"
        ordering = ["-create"]

    def __str__(self):
        return self.age


class Operational_System(models.Model):
    STATUS = (
        ('disponivel', 'Disponivel'),
        ('indisponivel', 'Indisponivel')
    ) 

    name = models.CharField(max_length=100, verbose_name='Sistema operacional')
    published = models.DateTimeField(default=now, verbose_name='Publicado')
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)

    def get_absolute_url_update5(self):
        return reverse('system_edit', args=[self.pk])

    class Meta:
        verbose_name = "Adicionar Sistema Operacional"
        verbose_name_plural = "Adicionar Sistema Operacional"
        ordering = ["-create"]

    def __str__(self):
        return self.name


class Graphics_Engine(models.Model):
    STATUS = (
        ('disponivel', 'Disponivel'),
        ('indisponivel', 'Indisponivel')
    ) 

    name = models.CharField(max_length=100, verbose_name='motor gráfico')
    published = models.DateTimeField(default=now, verbose_name='Publicado')
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)

    def get_absolute_url_update6(self):
        return reverse('engine_edit', args=[self.pk])

    class Meta:
        verbose_name = "Motor Gráfico"
        verbose_name_plural = "Motor Gráfico"
        ordering = ["-create"]

    def __str__(self):
        return self.name


class Designer(models.Model):
    STATUS = (
        ('disponível', 'Disponível'),
        ('indisponível', 'Indisponível')
    )

    name = models.CharField(max_length=100, verbose_name='Designer')
    published = models.DateTimeField(default=now, verbose_name='Publicado')
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)

    def get_absolute_url_update7(self):
        return reverse('designer_edit', args=[self.pk])
    class Meta:
        verbose_name = "designer"
        verbose_name_plural = "designer"
        ordering = ["-create"]

    def __str__(self):
        return self.name


class Select_Language(models.Model):
    STATUS = (
        ('disponível', 'Disponível'),
        ('indisponível', 'Indisponível')
    )

    name = models.CharField(max_length=100, verbose_name='Idioma')
    published = models.DateTimeField(default=now, verbose_name='Publicado')
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)

    def get_absolute_url_update8(self):
        return reverse('language_edit', args=[self.pk])
    class Meta:
        verbose_name = "Adicionar Linguagem"
        verbose_name_plural = "Adicionar Linguagem"
        ordering = ["-create"]

    def __str__(self):
        return self.name



class MinimumRequirements(models.Model):
    STATUS = (
        ('disponível', 'Disponível'),
        ('indisponível', 'Indisponível')
    )

    name = models.CharField(max_length=100, verbose_name='Requisitos Minimos')
    published = models.DateTimeField(default=now, verbose_name='Publicado')
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)

    def get_absolute_url_update9(self):
        return reverse('min_requirements_edit', args=[self.pk])
    class Meta:
        verbose_name = "Requisitos Minimos"
        verbose_name_plural = "Requisitos Minimos"
        ordering = ["-create"]

    def __str__(self):
        return self.description


class RecommendedRequirements(models.Model):
    STATUS = (
        ('disponível', 'Disponível'),
        ('indisponível', 'Indisponível')
    )

    name = models.CharField(max_length=100, verbose_name='Requisitos Recomendados')
    published = models.DateTimeField(default=now, verbose_name='Publicado')
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)

    def get_absolute_url_update10(self):
        return reverse ('max_requirements_edit', args=[self.pk])
    class Meta:
        verbose_name = "Requisitos Recomendados"
        verbose_name_plural = "Requisitos Recomendados"
        ordering = ["-create"]

    def __str__(self):
        return self.description



class Player(models.Model):
    STATUS = (
        ('disponível', 'Disponível'),
        ('indisponível', 'Indisponível')
    )

    name = models.CharField(max_length=100, verbose_name='Número de Jogadores')
    published = models.DateTimeField(default=now, verbose_name='Publicado')
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)

    def get_absolute_url_update11(self):
        return reverse ('player_edit', args=[self.pk])
    class Meta:
        verbose_name = "Número de Jogadores"
        verbose_name_plural = "Número de Jogadores"
        ordering = ["-create"]

    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS = (
        ('disponivel', 'Disponivel'),
        ('indisponivel', 'Indisponivel')
    )       

    title = models.CharField(max_length=200, verbose_name='Título do jogo',  null=False, blank=False)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)

    genre = models.ForeignKey('GameCategory', on_delete=models.CASCADE,default=GameCategory ,verbose_name='Gênero', blank=True, null=True)
    image = models.ImageField(upload_to='general_post', blank=False, null=True, verbose_name='Imagem')
    description = RichTextField(max_length=500, verbose_name='Descrição', blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='disponivel',  null=True)
    
    published = models.DateTimeField(default=now, null=True, verbose_name='Publicado' ,blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, verbose_name='Editora', blank=True, null=True)

    Operational_System = models.ForeignKey('Operational_System', on_delete=models.CASCADE, verbose_name='Sistema Operacional', blank=True, null=True)
    servant = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    Changed = models.DateTimeField(auto_now=True, blank=True, null=True)
    Select_Language = models.ManyToManyField(Select_Language, related_name="get_posts", verbose_name='Linguagens', blank=True, null=True)
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor', null=True)

    age_range = models.ForeignKey('Age_Range', on_delete=models.CASCADE, verbose_name='Faixa Etária', blank=True, null=True)
    graphics_engine =  models.ManyToManyField(Graphics_Engine, related_name="get_posts", verbose_name='Motor Gráfico', blank=True, null=True)
    designer = models.ManyToManyField(Designer, related_name="get_posts", verbose_name='Projetista', blank=True, null=True)
    player = models.ForeignKey('Player', on_delete=models.CASCADE, verbose_name='Número de Jogadores', blank=True, null=True)
    minimum_requirements = models.ForeignKey('MinimumRequirements', on_delete=models.CASCADE, verbose_name='Requisitos Minimos', blank=True, null=True)
    recommended_requirements = models.ForeignKey('RecommendedRequirements', on_delete=models.CASCADE, verbose_name='Requisitos Recomendados', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_absolute_url2(self):
        return reverse('home', )
        
    def get_absolute_url_update(self):
        return reverse('post_edit', args=[self.slug])

    def get_absolute_url_delete(self):
        return reverse('post_delete', args=[self.pk])

    class Meta:
        verbose_name = "Adicionar Jogo"
        verbose_name_plural = "Adicionar Jogos"

    def __str__(self):
        return str(self.title).capitalize()


@receiver(post_save, sender=Post)
def insert_slug(sender, instance, **kwargs):# def para gerar o slug automatico para não dá erro
    if kwargs.get('created', False):
        print('Criando slug')
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance.save()
