# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 03:34
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20170403_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('name', models.CharField(max_length=240)),
                ('email', models.CharField(max_length=240)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Product Answer',
                'verbose_name_plural': 'Product Answers',
                'ordering': ['-date_added'],
            },
        ),
        migrations.RemoveField(
            model_name='productvariation',
            name='description',
        ),
        migrations.RemoveField(
            model_name='productvariation',
            name='description_en_us',
        ),
        migrations.RemoveField(
            model_name='productvariation',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='productvariation',
            name='description_uk',
        ),
        migrations.AddField(
            model_name='product',
            name='composition',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Composition'),
        ),
        migrations.AddField(
            model_name='product',
            name='composition_en_us',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Composition'),
        ),
        migrations.AddField(
            model_name='product',
            name='composition_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Composition'),
        ),
        migrations.AddField(
            model_name='product',
            name='composition_uk',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Composition'),
        ),
        migrations.AddField(
            model_name='product',
            name='details',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='product',
            name='details_en_us',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='product',
            name='details_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='product',
            name='details_uk',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='product',
            name='htu',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='How to use'),
        ),
        migrations.AddField(
            model_name='product',
            name='htu_en_us',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='How to use'),
        ),
        migrations.AddField(
            model_name='product',
            name='htu_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='How to use'),
        ),
        migrations.AddField(
            model_name='product',
            name='htu_uk',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='How to use'),
        ),
        migrations.AddField(
            model_name='productanswer',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductVariation'),
        ),
    ]