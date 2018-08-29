# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20180829_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='day',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='weight',
            name='month',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='weight',
            name='year',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
