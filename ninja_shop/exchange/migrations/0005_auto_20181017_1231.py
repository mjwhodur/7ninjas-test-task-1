# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0004_auto_20181017_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ReferenceNumber',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
