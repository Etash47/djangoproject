# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitting', '0007_auto_20170317_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='location',
            field=models.CharField(default='A fake location', max_length=500, null=True, verbose_name='Location on Disk'),
        ),
    ]