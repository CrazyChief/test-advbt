# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 12:29
from __future__ import unicode_literals

import bloggiz.models
from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bloggiz', '0014_auto_20170717_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cropping',
        ),
        migrations.AlterField(
            model_name='post',
            name='cover_picture',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to=bloggiz.models.upload_path),
        ),
    ]
