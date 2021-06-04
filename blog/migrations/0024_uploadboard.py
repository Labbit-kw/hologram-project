# Generated by Django 2.2.2 on 2019-07-01 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20190627_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('filesize', models.IntegerField(default=0)),
                ('down', models.IntegerField(default=0)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]