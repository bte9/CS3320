# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20161202_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='name',
            new_name='description',
        ),
    ]
