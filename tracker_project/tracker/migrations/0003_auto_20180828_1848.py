# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_weight'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weight',
            old_name='weight',
            new_name='mass',
        ),
    ]
