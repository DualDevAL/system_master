# Generated by Django 3.2 on 2021-04-19 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general_post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='general_post', verbose_name='Imagem'),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('disponível', 'Disponível'), ('indisponível', 'Indisponível')], default='disponível', max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]