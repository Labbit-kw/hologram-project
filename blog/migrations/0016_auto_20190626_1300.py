# Generated by Django 2.2.2 on 2019-06-26 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190626_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]