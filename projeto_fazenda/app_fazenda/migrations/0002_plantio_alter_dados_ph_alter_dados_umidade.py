# Generated by Django 5.1.1 on 2024-09-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_fazenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plantio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('umidade_recomendado', models.FloatField()),
                ('ph_recomendado', models.FloatField()),
                ('texto_recomendacao', models.TextField(max_length=1200)),
            ],
        ),
        migrations.AlterField(
            model_name='dados',
            name='ph',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='dados',
            name='umidade',
            field=models.FloatField(),
        ),
    ]
