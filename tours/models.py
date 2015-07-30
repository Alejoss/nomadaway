from django.db import models

from ciudades.models import Ciudad
from perfiles.models import Perfil


class Tour(models.Model):
	ciudad = models.ForeignKey(Ciudad)
	punto_encuentro = models.ForeignKey('PuntoEncuentro')
	guia = models.ForeignKey(Perfil)
	descripcion = models.CharField(max_length=5000, blank=True)
	video_youtube = models.URLField(blank=True)


class PuntoEncuentro(models.Model):
	# El punto de encuentro del cual parte el Tour
	descripcion = models.CharField(max_length=1000, blank=True)
	coordenadas = models.CharField(max_length=200, blank=True)
	lugar = models.ForeignKey(Tour)


class FotosTour(models.Model):
	foto = models.URLField()
	tour = models.ForeignKey(Tour)
	perfil = models.ForeignKey(Perfil)
	descripcion = models.CharField(blank=True)
