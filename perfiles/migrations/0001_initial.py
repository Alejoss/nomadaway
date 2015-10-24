# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ciudades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=500, blank=True)),
                ('status', models.CharField(max_length=140, blank=True)),
                ('es_guia', models.BooleanField(default=False)),
                ('avatar', models.URLField(blank=True)),
                ('ciudad_actual', models.ForeignKey(related_name='actual', to='ciudades.Ciudad', null=True)),
                ('ciudad_origen', models.ForeignKey(related_name='origen', to='ciudades.Ciudad', null=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
