# Generated by Django 3.2 on 2021-05-07 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_post', '0010_auto_20210505_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='age_range',
            field=models.ManyToManyField(null=True, related_name='get_posts', to='general_post.Age_Range', verbose_name='Faixa Etária'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publisher',
            field=models.ManyToManyField(null=True, related_name='get_posts', to='general_post.Publisher', verbose_name='Editora'),
        ),
    ]
