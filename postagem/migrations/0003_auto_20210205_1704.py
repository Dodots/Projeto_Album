# Generated by Django 3.1.6 on 2021-02-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postagem', '0002_postagem_publicada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='foto_postagem',
            field=models.FileField(upload_to=''),
        ),
    ]
