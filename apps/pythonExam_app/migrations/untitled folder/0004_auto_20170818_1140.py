# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-18 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonExam_app', '0003_auto_20170818_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelplan',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
