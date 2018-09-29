# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-28 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipix', '0004_image_photos_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='ipix.Category'),
        ),
    ]