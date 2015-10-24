# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy

from models import Perfil


@login_required
def perfil(request, username):
	template = 'perfiles/perfil_propio.html'
	
	perfil, creado = Perfil.objects.get_or_create(usuario=request.user)

	context = {'perfil': perfil}

	return render(request, template, context)


class EditarPerfil(UpdateView):
	template_name = "perfiles/editar_perfil.html"	
	model = Perfil
	fields = ['descripcion']

	def get_object(self):
		perfil = Perfil.objects.get(usuario=self.request.user)
		return perfil
	
	def get_success_url(self):
		url = reverse_lazy('perfiles:propio', kwargs={'username': self.request.user.username})
		return url
