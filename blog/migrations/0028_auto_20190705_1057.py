# Generated by Django 2.2.2 on 2019-07-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_uploadboard_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadmin',
            name='user_id',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]