# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-05 03:24
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.TextField()),
                ('opening_hours', models.TextField()),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
                ('location', django.contrib.gis.db.models.fields.PointField(default='POINT(0.0 0.0)', geography=True, srid=4326)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='hospital',
            unique_together=set([('name', 'address', 'location')]),
        ),
    ]
