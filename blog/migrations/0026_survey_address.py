# Generated by Django 2.2.2 on 2019-07-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20190702_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
