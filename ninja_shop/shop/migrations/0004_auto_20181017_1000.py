# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181016_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverypricelist',
            name='Currency',
        ),
        migrations.RemoveField(
            model_name='deliverypricelist',
            name='DeliveryMethod',
        ),
        migrations.RemoveField(
            model_name='orderpositions',
            name='Order',
        ),
        migrations.RemoveField(
            model_name='orderpositions',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='productpricelist',
            name='Currency',
        ),
        migrations.RemoveField(
            model_name='productpricelist',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Currency',
        ),
        migrations.AddField(
            model_name='deliverytype',
            name='Price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='Count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='Product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='shop.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='MethodOfDelivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.DeliveryType'),
        ),
        migrations.DeleteModel(
            name='Currencies',
        ),
        migrations.DeleteModel(
            name='DeliveryPriceList',
        ),
        migrations.DeleteModel(
            name='OrderPositions',
        ),
        migrations.DeleteModel(
            name='ProductPriceList',
        ),
    ]
