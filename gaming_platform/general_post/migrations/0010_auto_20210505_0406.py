# Generated by Django 3.2 on 2021-05-05 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_post', '0009_auto_20210505_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='age_range',
        ),
        migrations.AlterField(
            model_name='post',
            name='publisher',
            field=models.ManyToManyField(null=True, related_name='get_posts', to='general_post.Publisher', verbose_name='Editora'),
        ),
    ]