# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-14 22:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloggiz', '0010_auto_20170410_0445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content_en_us',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_uk',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pretext_en_us',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pretext_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pretext_uk',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_en_us',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_uk',
        ),
    ]
