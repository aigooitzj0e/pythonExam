# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-19 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonExam_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='many_users',
            field=models.ManyToManyField(related_name='all_plans', to='pythonExam_app.User'),
        ),
    ]
