# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_objeto', models.PositiveSmallIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.CharField(max_length=1000)),
                ('tiene_respuestas', models.BooleanField(default=False)),
                ('eliminado', models.BooleanField(default=False)),
                ('muro', models.ForeignKey(to='posts.Muro')),
                ('perfil', models.ForeignKey(to='perfiles.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.CharField(max_length=1000)),
                ('eliminado', models.BooleanField(default=False)),
                ('perfil', models.ForeignKey(to='perfiles.Perfil')),
                ('post', models.ForeignKey(to='posts.Post')),
            ],
        ),
    ]
