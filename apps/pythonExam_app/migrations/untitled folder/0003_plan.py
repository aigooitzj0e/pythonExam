# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-18 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pythonExam_app', '0002_auto_20170818_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='pythonExam_app.User')),
            ],
        ),
    ]