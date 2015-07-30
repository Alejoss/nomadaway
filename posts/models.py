from django.db import models

from perfiles.models import Perfil


class Post(models.Model):
	texto = models.CharField(max_length=1000)
	perfil = models.ForeignKey(Perfil)
	parent = # Problema - Posiblemente usar ContentTypes https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/
	tiene_respuestas = models.BooleanField(default=False)
	eliminado = models.BooleanField(default=False)


class Respuesta(models.Model):
	post = models.ForeignKey(Post)
	texto = models.CharField(max_length=1000)
	perfil = models.ForeignKey(Perfil)
	eliminado = models.BooleanField(default=False)
