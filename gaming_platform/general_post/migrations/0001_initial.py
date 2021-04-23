# Generated by Django 3.2 on 2021-04-20 03:21

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('servant', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='Título do jogo')),
                ('slug', models.SlugField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='general_post', verbose_name='Imagem')),
                ('description', ckeditor.fields.RichTextField(max_length=500, null=True, verbose_name='Descrição')),
                ('status', models.CharField(choices=[('disponivel', 'Disponivel'), ('indisponivel', 'Indisponivel')], default='disponível', max_length=15, null=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Publicado')),
                ('servant', models.DateTimeField(auto_now_add=True)),
                ('Changed', models.DateTimeField(auto_now=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Valor')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('category', models.ManyToManyField(related_name='get_posts', to='general_post.GameCategory', verbose_name='Categoria')),
            ],
        ),
    ]
