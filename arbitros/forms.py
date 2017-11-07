from django.contrib.admin import widgets
from django import forms
from .models import Partido, Arbitro, Agenda

class AgendaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Agenda
        fields = ('arbitro', 'partido')
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.
def __init__ (self, *args, **kwargs):
        super(AgendaForm, self).__init__(*args, **kwargs)
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["arbitro"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["arbitro"].help_text = "Escoja el doctor a citar"
#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["arbitro"].queryset = Arbitro.objects.all()
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["partido"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["partido"].help_text = "Seleccione el partido asignado"
#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["partido"].queryset = Partrido.objects.all()

#-----------------Partido--------------------

class PartidoForm(forms.ModelForm):

    class Meta:
        model = Partido
        fields = ('nombre', 'descripcion', 'fecha',)

#-----------------Arbitro--------------------

class ArbitroForm(forms.ModelForm):

    class Meta:
        model = Arbitro
        fields = ('nombre', 'telefono',)
