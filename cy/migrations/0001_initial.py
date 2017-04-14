# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('abbreviation', models.CharField(max_length=6, unique=True, verbose_name='Abbreviation')),
                ('symbol', models.CharField(max_length=1, unique=True, verbose_name='Symbol')),
                ('dimension', models.DecimalField(decimal_places=10, max_digits=19, verbose_name='Dimension')),
                ('base', models.BooleanField(default=False, verbose_name='Base')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
    ]
