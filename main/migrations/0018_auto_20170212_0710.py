# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20170212_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentication',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]
