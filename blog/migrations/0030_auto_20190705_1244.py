# Generated by Django 2.2.2 on 2019-07-05 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20190705_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadboard',
            old_name='file_title',
            new_name='title',
        ),
    ]
