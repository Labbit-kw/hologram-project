# Generated by Django 2.2.2 on 2019-06-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_postadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadmin',
            name='user_id',
            field=models.CharField(blank=True, default='chansoopark', max_length=20),
        ),
        migrations.AlterField(
            model_name='postadmin',
            name='user_pw',
            field=models.CharField(blank=True, default='1234', max_length=20),
        ),
    ]