from django.conf.urls import url

import views

urlpatterns = [
	url(r'^editar_perfil/$', views.EditarPerfil.as_view(), name="editar_perfil"),
	url(r'^p/(?P<username>[-\w.]+)/$', views.perfil, name="propio")
]
