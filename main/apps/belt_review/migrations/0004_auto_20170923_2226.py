# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-23 22:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_review', '0003_auto_20170923_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='raiting',
            new_name='rating',
        ),
    ]