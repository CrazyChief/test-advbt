# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20170801_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AddField(
            model_name='productvariation',
            name='sku',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name='Sku'),
        ),
    ]