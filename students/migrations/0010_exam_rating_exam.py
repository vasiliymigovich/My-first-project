# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20160228_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='rating_exam',
            field=models.ManyToManyField(max_length=10, null=True, to='students.Student', verbose_name='\u041e\u0446\u0456\u043d\u043a\u0430'),
        ),
    ]
