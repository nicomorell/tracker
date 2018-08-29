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
                ('age', models.PositiveIntegerField(blank=True)),
                ('heightFeet', models.FloatField(blank=True)),
                ('heightInches', models.FloatField(null=True, blank=True)),
                ('heightMetres', models.FloatField(blank=True)),
                ('weightPounds', models.FloatField(null=True, blank=True)),
                ('weightKilos', models.FloatField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mass', models.FloatField(null=True, blank=True)),
                ('day', models.PositiveIntegerField(null=True, blank=True)),
                ('month', models.PositiveIntegerField(null=True, blank=True)),
                ('year', models.PositiveIntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
