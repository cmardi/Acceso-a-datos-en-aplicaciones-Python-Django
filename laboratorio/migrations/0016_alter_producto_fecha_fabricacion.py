# Generated by Django 5.1.4 on 2025-01-18 03:20

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0015_alter_producto_laboratorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_fabricacion',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2015, 1, 1, 3, 0, tzinfo=datetime.timezone.utc))]),
        ),
    ]
