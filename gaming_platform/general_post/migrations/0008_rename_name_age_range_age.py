# Generated by Django 3.2 on 2021-05-04 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_post', '0007_rename_age_age_range_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='age_range',
            old_name='name',
            new_name='age',
        ),
    ]