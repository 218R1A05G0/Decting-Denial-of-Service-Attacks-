# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-16 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_admins', '0005_delete_ddos_attacks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ddos_dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddos_data', models.CharField(max_length=500)),
                ('attack_result', models.CharField(max_length=500)),
            ],
        ),
    ]