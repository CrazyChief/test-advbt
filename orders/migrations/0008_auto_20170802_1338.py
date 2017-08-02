# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_order_discount_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_departament',
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_type',
            field=models.CharField(choices=[('USA_S', 'USA Shipping'), ('I_S', 'International Shipping (We will call you back to clarify the details)')], default='I_S', max_length=50),
        ),
    ]
