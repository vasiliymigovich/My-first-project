# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-28 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_exam_examiner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='date_exam',
            field=models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0456 \u0447\u0430\u0441 \u0435\u043a\u0437\u0430\u043c\u0435\u043d\u0443'),
        ),
    ]
