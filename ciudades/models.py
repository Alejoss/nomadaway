from django.db import models
from cities_light.models import City


class Ciudad(models.Model):
	city_obj = models.ForeignKey(City)  # Usamos una librería externa para poblar la db de las ciudades del mundo
	portada = models.URLField(blank=True)
	activa = models.BooleanField
	num_tours = models.IntegerField(default=0)
	num_lugares = models.IntegerField(default=0)
	prioridad = models.SmallIntegerField(default=0)  # Para mostrar eficientemente tours & lugares cercanos
