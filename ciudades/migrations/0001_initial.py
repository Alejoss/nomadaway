# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0004_auto_20150804_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('portada', models.URLField(blank=True)),
                ('num_tours', models.IntegerField(default=0)),
                ('num_lugares', models.IntegerField(default=0)),
                ('prioridad', models.SmallIntegerField(default=0)),
                ('city_obj', models.ForeignKey(to='cities_light.City')),
            ],
        ),
    ]
