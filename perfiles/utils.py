
from perfiles.models import Perfil


def obtener_perfil(user):

	perfil, creado = Perfil.objects.get_or_create(usuario=user)
