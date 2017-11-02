# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20171031_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='entrance_grade1',
            field=models.IntegerField(blank=True, null=True, verbose_name='语文成绩'),
        ),
        migrations.AlterField(
            model_name='student',
            name='entrance_grade2',
            field=models.IntegerField(blank=True, null=True, verbose_name='数学成绩'),
        ),
        migrations.AlterField(
            model_name='student',
            name='entrance_grade3',
            field=models.IntegerField(blank=True, null=True, verbose_name='英语成绩'),
        ),
        migrations.AlterField(
            model_name='student',
            name='entrance_grade4',
            field=models.IntegerField(blank=True, null=True, verbose_name='政治成绩'),
        ),
        migrations.AlterField(
            model_name='student',
            name='entrance_grade5',
            field=models.IntegerField(blank=True, null=True, verbose_name='历史成绩'),
        ),
    ]