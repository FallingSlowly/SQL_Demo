# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20171031_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalgrade',
            name='s_grade',
            field=models.IntegerField(blank=True, null=True, verbose_name='成绩'),
        ),
    ]