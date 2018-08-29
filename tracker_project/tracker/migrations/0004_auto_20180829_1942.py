# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20180828_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='mass',
            field=models.FloatField(blank=True),
        ),
    ]
