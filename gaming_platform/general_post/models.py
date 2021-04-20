from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    STATUS = (
        ('disponivel', 'Disponivel'),
        ('indisponivel', 'Indisponivel')

    )

    title = models.CharField(max_length=200, verbose_name='Título do jogo',  null=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'general_post', null=True, verbose_name='Imagem')
    description = models.TextField(max_length=500, verbose_name='Descrição', null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='disponível',  null=True)
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor', null=True,)

    '''class Meta:
        ordering = ('-disponivel',)'''

    def __str__(self):
        return str(self.title).capitalize()
