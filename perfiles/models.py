# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from ciudades.models import Ciudad


class Perfil(models.Model):
	usuario = models.ForeignKey(User)
	descripcion = models.CharField(max_length=500, blank=True)
	status = models.CharField(max_length=140, blank=True)  # Estado similar el estado de facebook pero que responde a otra pregunta.
	es_guia = models.BooleanField(default=False)
	ciudad_origen = models.ForeignKey(Ciudad, related_name="origen", null=True)
	ciudad_actual = models.ForeignKey(Ciudad, related_name="actual", null=True)
	avatar = models.URLField(blank=True)
