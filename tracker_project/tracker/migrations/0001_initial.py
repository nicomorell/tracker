# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BMI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.PositiveIntegerField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
