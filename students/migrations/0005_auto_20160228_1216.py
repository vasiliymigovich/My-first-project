# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-28 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_exam_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='title_exam',
            field=models.CharField(max_length=45, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443'),
        ),
    ]
