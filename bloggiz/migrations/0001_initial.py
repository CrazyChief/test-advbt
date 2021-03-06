# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 16:12
from __future__ import unicode_literals

import bloggiz.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Author')),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(verbose_name='Comment')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bloggiz.Comments', verbose_name='Parent')),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'ordering': ['date_added'],
                'verbose_name': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(null=True)),
                ('cover_picture', models.ImageField(blank=True, upload_to=bloggiz.models.upload_path)),
                ('cropping', image_cropping.fields.ImageRatioField('cover_picture', '300x430', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('is_published', models.BooleanField(choices=[(True, 'Published'), (False, 'Draft')], default=False, verbose_name='Is published')),
                ('pretext', models.TextField(verbose_name='Short content')),
                ('content', models.TextField(verbose_name='Content')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'ordering': ['-date_added'],
                'verbose_name': 'Post',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloggiz.Post'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
