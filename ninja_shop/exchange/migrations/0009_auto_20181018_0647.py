# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-18 06:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0008_auto_20181018_0628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverytype',
            name='IsPercent',
        ),
        migrations.RemoveField(
            model_name='deliverytype',
            name='PercentValue',
        ),
    ]