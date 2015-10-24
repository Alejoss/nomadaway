# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
        ('ciudades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotosTour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.URLField()),
                ('descripcion', models.CharField(max_length=500, blank=True)),
                ('perfil', models.ForeignKey(to='perfiles.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='PuntoEncuentro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=1000, blank=True)),
                ('coordenadas', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=5000, blank=True)),
                ('video_youtube', models.URLField(blank=True)),
                ('ciudad', models.ForeignKey(to='ciudades.Ciudad')),
                ('guia', models.ForeignKey(to='perfiles.Perfil')),
                ('punto_encuentro', models.ForeignKey(to='tours.PuntoEncuentro')),
            ],
        ),
        migrations.AddField(
            model_name='puntoencuentro',
            name='lugar',
            field=models.ForeignKey(to='tours.Tour'),
        ),
        migrations.AddField(
            model_name='fotostour',
            name='tour',
            field=models.ForeignKey(to='tours.Tour'),
        ),
    ]
