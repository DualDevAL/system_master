# Generated by Django 3.2 on 2021-04-20 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
