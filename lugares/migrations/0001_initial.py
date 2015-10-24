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
            name='FotosLugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.URLField()),
                ('descripcion', models.CharField(max_length=500, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=5000)),
                ('coordenadas', models.CharField(max_length=200, blank=True)),
                ('ciudad', models.ForeignKey(to='ciudades.Ciudad')),
                ('perfil', models.ForeignKey(to='perfiles.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='PasoParaLlegar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=500, blank=True)),
                ('foto', models.URLField(blank=True)),
                ('num_paso', models.SmallIntegerField(default=1)),
                ('coordenadas', models.CharField(max_length=200, blank=True)),
                ('lugar', models.ForeignKey(to='lugares.Lugar')),
            ],
        ),
        migrations.AddField(
            model_name='fotoslugar',
            name='lugar',
            field=models.ForeignKey(to='lugares.Lugar'),
        ),
        migrations.AddField(
            model_name='fotoslugar',
            name='perfil',
            field=models.ForeignKey(to='perfiles.Perfil'),
        ),
    ]
