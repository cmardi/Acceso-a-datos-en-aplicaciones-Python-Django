# Generated by Django 5.1.4 on 2024-12-27 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0011_laboratorio_ciudad_laboratorio_pais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(max_length=255),
        ),
    ]
