from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

from ciudades import views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.main, name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^perfil/', include('perfiles.urls', namespace="perfiles")),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'extra_context': {'next': '/'}}, name="login"),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html', 'next_page': '/'}, name="logout"),
]
