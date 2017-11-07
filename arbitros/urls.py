from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^$', views.arbitro_lista),
    #url(r'^$', views.info_index),
    url(r'^arbitros', views.arbitro_lista, name = 'arbitro_lista'),
    url(r'^arbitro/(?P<pk>[0-9]+)/$', views.arbitro_detalle, name='arbitro_detalle'),
    url(r'^arbitro/nuevo/$', views.arbitro_nuevo, name='arbitro_nuevo'),
    url(r'^arbitro/(?P<pk>[0-9]+)/editar/$', views.arbitro_editar, name='arbitro_editar'),
    url(r'^arbitro/(?P<pk>\d+)/del/$', views.arbitro_del, name='arbitro_del'),
    url(r'^partidos/', views.partido_lista, name='partido_lista'),
    url(r'^partido/(?P<pk>[0-9]+)/$', views.partido_detalle, name='partido_detalle'),
    url(r'^partido/nuevo/$', views.partido_nuevo, name='partido_nuevo'),
    url(r'^partido/(?P<pk>[0-9]+)/editar/$', views.partido_editar, name='partido_editar'),
    url(r'^partido/(?P<pk>\d+)/del/$', views.partido_del, name='partido_del'),
    url(r'^$', views.agenda_lista, name='agenda_lista'),
    url(r'^agenda/(?P<pk>[0-9]+)/$', views.agenda_detalle, name='agenda_detalle'),
    url(r'^agenda/nueva/$', views.agenda_nueva, name='agenda_nueva'),
    url(r'^agenda/(?P<pk>[0-9]+)/editar/$', views.agenda_editar, name='agenda_editar'),
    url(r'^agenda/(?P<pk>\d+)/del/$', views.agenda_del, name='agenda_del'),
]
