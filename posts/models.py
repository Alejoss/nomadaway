from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from perfiles.models import Perfil


class Muro(models.Model):
	content_type = models.ForeignKey(ContentType)
	id_objeto = models.PositiveSmallIntegerField()
	content_object = GenericForeignKey('content_type', 'id_objeto')


class Post(models.Model):
	texto = models.CharField(max_length=1000)
	perfil = models.ForeignKey(Perfil)
	muro = models.ForeignKey(Muro)
	tiene_respuestas = models.BooleanField(default=False)
	eliminado = models.BooleanField(default=False)


class Respuesta(models.Model):
	post = models.ForeignKey(Post)
	texto = models.CharField(max_length=1000)
	perfil = models.ForeignKey(Perfil)
	eliminado = models.BooleanField(default=False)
