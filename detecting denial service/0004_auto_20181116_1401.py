# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-16 08:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_admins', '0003_ddos_attacks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ddos_attacks',
            old_name='links',
            new_name='analyis_results',
        ),
        migrations.RenameField(
            model_name='ddos_attacks',
            old_name='result',
            new_name='ddos_data',
        ),
    ]
