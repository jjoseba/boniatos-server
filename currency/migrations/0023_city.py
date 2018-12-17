# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-17 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0015_payment_concept'),
        ('currency', '0022_entity_percent_validators'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.CharField(editable=True, max_length=10, primary_key=True, serialize=False, verbose_name='Identificador')),
                ('shortname', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nombre corto')),
                ('full_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre completo')),
                ('latitude', models.FloatField(default=0, verbose_name='Latitud')),
                ('longitude', models.FloatField(default=0, verbose_name='Longitud')),
                ('server_base_url', models.CharField(default=0, max_length=250, verbose_name='URL Servidor Gesti\xf3n')),
                ('facebook_link', models.CharField(blank=True, max_length=250, null=True, verbose_name='P\xe1gina de Facebook')),
                ('webpage_link', models.CharField(blank=True, max_length=250, null=True, verbose_name='P\xe1gina web')),
                ('twitter_link', models.CharField(blank=True, max_length=250, null=True, verbose_name='Perfil de Twitter')),
                ('telegram_link', models.CharField(blank=True, max_length=250, null=True, verbose_name='Canal de Telegram')),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_debit', to='wallets.Wallet', verbose_name='Monedero de d\xe9bito')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Mercado social',
                'verbose_name_plural': 'Mercados sociales',
            },
        ),
    ]