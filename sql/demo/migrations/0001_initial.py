# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.IntegerField(verbose_name='课程号')),
                ('class_name', models.CharField(max_length=100, verbose_name='课程名称')),
                ('class_credit', models.IntegerField(verbose_name='学分')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='GeneralGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_grade', models.IntegerField(verbose_name='成绩')),
                ('s_subject', models.IntegerField(verbose_name='课程号')),
                ('s_number', models.IntegerField(verbose_name='学号')),
            ],
            options={
                'verbose_name': '成绩',
                'verbose_name_plural': '成绩',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.IntegerField(verbose_name='学生学号')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('gender', models.CharField(max_length=10, verbose_name='性别')),
                ('birth_date', models.DateField(verbose_name='出生日期')),
                ('entrance_grade1', models.IntegerField(verbose_name='语文成绩')),
                ('entrance_grade2', models.IntegerField(verbose_name='数学成绩')),
                ('entrance_grade3', models.IntegerField(verbose_name='英语成绩')),
                ('entrance_grade4', models.IntegerField(verbose_name='政治成绩')),
                ('entrance_grade5', models.IntegerField(verbose_name='历史成绩')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
    ]