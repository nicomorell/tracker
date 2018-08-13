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
                ('heightFeet', models.FloatField()),
                ('heightInches', models.FloatField(null=True, blank=True)),
                ('heightMetres', models.PositiveIntegerField(blank=True)),
                ('weightPounds', models.FloatField(null=True, blank=True)),
                ('weightKilos', models.FloatField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
