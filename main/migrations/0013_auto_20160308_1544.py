# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20160308_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='security',
            name='OriginalAcceptedDate',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='security',
            name='OriginalSentDate',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]