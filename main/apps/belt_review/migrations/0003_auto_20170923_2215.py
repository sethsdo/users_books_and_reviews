# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-23 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_review', '0002_auto_20170923_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='books_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_id', to='belt_review.book'),
        ),
    ]
