from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    STATUS = (
        ('disponível', 'Disponível'),
        ('indisponível', 'Indisponível')

    )

    title = models.CharField(max_length=200, verbose_name='Título do jogo')
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'general_post', blank=True, null=True, verbose_name='Imagem')

    status = models.CharField(max_length=15, choices=STATUS, default='disponível')

    @property
    def views_image(self):
        return mark_safe('<img scr="%s" width="400px" />' % self.imagem.url)
       # view_image.short_description = "Imagem Cadastrada"
       # view_image.allow_tags = True

    #class Meta:
     #   ordering = ('-disponível',)

    def __str__(self):
        return str(self.title).capitalize()

