# Generated by Django 2.2.15 on 2020-09-21 14:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0003_product_shipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shipment',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]