# -*- coding: utf-8 -*-
from django.db import models

from ciudades.models import Ciudad
from perfiles.models import Perfil


class Lugar(models.Model):
	# Un lugar puede ser un mirador, una cascada, un un bar
	nombre = models.CharField(max_length=150)
	ciudad = models.ForeignKey(Ciudad)
	perfil = models.ForeignKey(Perfil)
	descripcion = models.CharField(max_length=5000)
	coordenadas = models.CharField(max_length=200, blank=True)


class PasoParaLlegar(models.Model):
	# Describe cómo llegar a un lugar, un Lugar puede tener varios pasos para llegar
	lugar = models.ForeignKey(Lugar)
	descripcion = models.CharField(max_length=500, blank=True)
	foto = models.URLField(blank=True)
	num_paso = models.SmallIntegerField(default=1)
	coordenadas = models.CharField(max_length=200, blank=True)


class FotosLugar(models.Model):
	foto = models.URLField()
	lugar = models.ForeignKey(Lugar)
	perfil = models.ForeignKey(Perfil)
	descripcion = models.CharField(max_length=500, blank=True)
