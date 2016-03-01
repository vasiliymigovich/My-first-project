# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-25 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_exam', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443')),
                ('date_exam', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0435\u043a\u0437\u0430\u043c\u0435\u043d\u0443')),
            ],
            options={
                'verbose_name': '\u0406\u0441\u043f\u0438\u0442\u0438',
                'verbose_name_plural': '\u0406\u0441\u043f\u0438\u0442\u0438',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '\u0412\u0456\u0434\u0432\u0456\u0434\u0443\u0432\u0430\u043d\u043d\u044f',
                'verbose_name_plural': '\u0412\u0456\u0434\u0432\u0456\u0434\u0443\u0432\u0430\u043d\u043d\u044f',
            },
        ),
    ]
