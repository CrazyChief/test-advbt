# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_subcategory_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sub_categories',
        ),
        migrations.AddField(
            model_name='product',
            name='sub_categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.SubCategory', verbose_name='Sub categories'),
        ),
    ]