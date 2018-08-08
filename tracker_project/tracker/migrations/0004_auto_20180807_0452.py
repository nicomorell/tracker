# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20180807_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmi',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='heightFeet',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='heightInches',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='weightPounds',
            field=models.FloatField(),
        ),
    ]
