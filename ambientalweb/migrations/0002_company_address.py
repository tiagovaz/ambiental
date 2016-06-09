# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-03 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambientalweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ambientalweb.Address'),
            preserve_default=False,
        ),
    ]
