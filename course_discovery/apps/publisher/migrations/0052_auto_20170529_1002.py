# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-29 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0051_auto_20170525_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalseat',
            name='credit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='seat',
            name='credit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
