# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-12 05:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_auto_20160812_1122'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='monthlyworkingschedule',
            unique_together=set([('month', 'year')]),
        ),
    ]
