from django.db import models
from django.contrib import admin

class Arbitro(models.Model):
    nombre  =   models.CharField(max_length=30)
    telefono = models.CharField(max_length=15, blank=False, null=True)
    def __str__(self):
        return self.nombre

class Partido(models.Model):
    nombre    = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    fecha = models.CharField(max_length=12)
    def __str__(self):
        return self.nombre

class Agenda(models.Model):
    arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)

class AgendaInLine(admin.TabularInline):
    model = Agenda
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class PartidoAdmin(admin.ModelAdmin):
    inlines = (AgendaInLine,)

class ArbitroAdmin(admin.ModelAdmin):
    inlines = (AgendaInLine,)
