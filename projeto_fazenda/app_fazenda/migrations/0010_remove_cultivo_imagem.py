# Generated by Django 5.1.1 on 2024-10-05 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_fazenda', '0009_cultivo_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cultivo',
            name='imagem',
        ),
    ]