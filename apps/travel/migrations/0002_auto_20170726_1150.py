# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
