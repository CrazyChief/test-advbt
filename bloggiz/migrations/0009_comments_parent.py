# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 01:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloggiz', '0008_auto_20170409_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bloggiz.Comments'),
        ),
    ]