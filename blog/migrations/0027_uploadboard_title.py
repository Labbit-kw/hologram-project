# Generated by Django 2.2.2 on 2019-07-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_survey_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadboard',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
