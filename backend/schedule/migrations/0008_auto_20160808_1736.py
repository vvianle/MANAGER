# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-08 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20160808_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyworkingschedule',
            name='month',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='monthlyworkingschedule',
            name='year',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
