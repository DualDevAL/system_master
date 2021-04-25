# Generated by Django 3.2 on 2021-04-25 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='general_post', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('disponivel', 'Disponivel'), ('indisponivel', 'Indisponivel')], default='disponivel', max_length=15, null=True),
        ),
    ]
