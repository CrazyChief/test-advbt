# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(choices=[(True, 'Published'), (False, 'Draft')], default=False)),
            ],
            options={
                'verbose_name_plural': 'Emails',
                'verbose_name': 'Email',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=300, null=True)),
                ('location', models.CharField(max_length=300, null=True)),
            ],
            options={
                'verbose_name_plural': 'Locations',
                'verbose_name': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_prefix', models.CharField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Phones',
                'verbose_name': 'Phone',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Reviews',
                'ordering': ['-date_added'],
                'verbose_name': 'Review',
            },
        ),
    ]
