# Generated by Django 2.2.1 on 2019-05-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='es_administrador',
            field=models.BooleanField(default=False),
        ),
    ]
