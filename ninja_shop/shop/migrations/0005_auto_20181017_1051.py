# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20181017_1000'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='UserName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='MethodOfDelivery',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='Contractor',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='Product',
        ),
        migrations.DeleteModel(
            name='Contractor',
        ),
        migrations.DeleteModel(
            name='DeliveryType',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='WishList',
        ),
    ]
