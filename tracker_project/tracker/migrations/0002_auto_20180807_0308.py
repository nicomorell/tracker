# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bmi',
            old_name='height',
            new_name='heightFeet',
        ),
        migrations.RenameField(
            model_name='bmi',
            old_name='weight',
            new_name='heightInches',
        ),
        migrations.AddField(
            model_name='bmi',
            name='weightPounds',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
