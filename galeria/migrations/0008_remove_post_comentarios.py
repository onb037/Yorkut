# Generated by Django 5.0.6 on 2024-07-01 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_post_comentarios_alter_post_privacidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comentarios',
        ),
    ]
