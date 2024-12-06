# Generated by Django 5.1.2 on 2024-11-01 08:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_is_sale_product_sale_price_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='star',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 11, 1, 12, 23, 28, 811537)),
        ),
    ]
