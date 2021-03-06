# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-18 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pythonExam_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travelplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='username',
        ),
        migrations.AddField(
            model_name='travelplan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travelplans', to='pythonExam_app.User'),
        ),
    ]
