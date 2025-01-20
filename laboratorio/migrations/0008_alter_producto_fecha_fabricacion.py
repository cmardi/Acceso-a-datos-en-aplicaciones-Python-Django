# Generated by Django 5.1.4 on 2024-12-21 01:16

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0007_alter_producto_fecha_fabricacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_fabricacion',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2015, 1, 1, 0, 0))]),
        ),
    ]
