# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-13 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0009_wallet_pin_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletType',
            fields=[
                ('id', models.CharField(editable=False, max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=150, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripci\xf3n')),
                ('credit_limit', models.FloatField(default=0, verbose_name='L\xedmite de cr\xe9dito')),
                ('unlimited', models.BooleanField(default=False, verbose_name='Cr\xe9dito ilimitado')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Tipo de cuenta',
                'verbose_name_plural': 'Tipos de cuenta',
            },
        ),
        migrations.AddField(
            model_name='wallet',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallets', to='wallets.WalletType'),
        ),
    ]
