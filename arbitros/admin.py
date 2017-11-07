from django.contrib import admin
from .models import Partido, PartidoAdmin, Arbitro, ArbitroAdmin, Agenda, AgendaInLine

#Registramos nuestras clases principales.
admin.site.register(Arbitro, ArbitroAdmin)
admin.site.register(Partido, PartidoAdmin)
admin.site.register(Agenda)
