# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_auto_20171010_1609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['timestamp'], 'verbose_name': 'Transacci\xf3n', 'verbose_name_plural': 'Transacciones'},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Timestamp'),
            preserve_default=False,
        ),
    ]
