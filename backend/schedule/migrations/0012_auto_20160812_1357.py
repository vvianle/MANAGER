# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-12 06:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0011_auto_20160812_1207'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='workingcalendar',
            unique_together=set([]),
        ),
    ]
