# Generated by Django 2.2.2 on 2019-06-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_survey'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='survey',
            options={'ordering': ('id',), 'verbose_name': 'survey', 'verbose_name_plural': 'surveys'},
        ),
        migrations.AlterField(
            model_name='survey',
            name='sex',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
