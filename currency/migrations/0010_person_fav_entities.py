# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0009_auto_20171010_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='fav_entities',
            field=models.ManyToManyField(blank=True, null=True, to='currency.Entity', verbose_name='Favoritos'),
        ),
    ]
