# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_remove_exam_rating_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='group_exam',
            field=models.ForeignKey(max_length=45, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Group', verbose_name='\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0433\u0440\u0443\u043f\u0443'),
        ),
    ]
