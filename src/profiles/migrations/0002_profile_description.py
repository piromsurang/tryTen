# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default='description default text'),
        ),
    ]
