from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import RequestContext
from .forms import AgendaForm, PartidoForm, ArbitroForm
from arbitros.models import Arbitro, Partido, Agenda
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


def agenda_lista(request):
    agendas = Agenda.objects.all
    return render(request, 'arbitros/agenda_lista.html', {'agendas':agendas})

def agenda_detalle(request, pk):
    agendas = get_object_or_404(Agenda, pk=pk)
    return render(request, 'arbitros/agenda_detalle.html', {'agendas': agendas})

@login_required
def agenda_nueva(request):
    if request.method == "POST":
        formulario = AgendaForm(request.POST)
        if formulario.is_valid():
            agenda = formulario.save(commit=False)
            for arbitro_id in request.POST.getlist('arbitro'):
                for partido_id in request.POST.getlist('partido'):
                    agenda = Agenda(arbitro_id=arbitro_id, partido_id = partido_id)
                    agenda.save()
        return redirect('arbitros.views.agenda_lista')
    else:
        formulario = AgendaForm()
    return render(request, 'arbitros/agenda_nueva.html', {'formulario': formulario})

@login_required
def agenda_editar(request, pk):
    agenda = get_object_or_404(Agenda, pk=pk)
    if request.method == "POST":
        formulario = AgendaForm(request.POST, instance=agenda)
        if formulario.is_valid():
            agenda = formulario.save(commit=False)
            for arbitro_id in request.POST.getlist('arbitro'):
                for partido_id in request.POST.getlist('partido'):
                    agenda.save()
        return redirect('arbitros.views.agenda_lista')
    else:
        formulario = AgendaForm(instance=agenda)
    return render(request, 'arbitros/agenda_editar.html', {'formulario': formulario})

@login_required
def agenda_del(request, pk):
    agenda = get_object_or_404(Agenda, pk=pk)
    agenda.delete()
    return redirect('arbitros.views.agenda_lista')


#-------------------------- Vista de Partido -----------------------------------

def partido_lista(request):
    partidos = Partido.objects.all
    return render(request, 'arbitros/partido_lista.html', {'partidos':partidos})

def partido_detalle(request, pk):
    partidos = get_object_or_404(Partido, pk=pk)
    return render(request, 'arbitros/partido_detalle.html', {'partidos': partidos})

@login_required
def partido_nuevo(request):
    if request.method == "POST":
        formulario = PartidoForm(request.POST)
        if formulario.is_valid():
            partido = formulario.save(commit=False)
            partido = Partido(nombre = formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'],fecha = formulario.cleaned_data['fecha'])
            partido.save()
        return redirect('partido_lista')
    else:
        formulario = PartidoForm()
    return render(request, 'arbitros/partido_nuevo.html', {'formulario': formulario})

@login_required
def partido_editar(request, pk):
    partido = get_object_or_404(Partido, pk=pk)
    if request.method == "POST":
        formulario = PartidoForm(request.POST, instance=partido)
        if formulario.is_valid():
            partido = formulario.save(commit=False)
            partido.save()
        return redirect('partido_lista')
    else:
        formulario = PartidoForm(instance=partido)
    return render(request, 'arbitros/partido_editar.html', {'formulario': formulario})

@login_required
def partido_del(request, pk):
    partido = get_object_or_404(Partido, pk=pk)
    partido.delete()
    return redirect('partido_lista')

#-------------------------- Vista de Arbitro-----------------------------------

def arbitro_lista(request):
    arbitros = Arbitro.objects.all
    return render(request, 'arbitros/arbitro_lista.html', {'arbitros':arbitros})

def arbitro_detalle(request, pk):
    arbitros = get_object_or_404(Arbitro, pk=pk)
    return render(request, 'arbitros/arbitro_detalle.html', {'arbitros': arbitros})

@login_required
def arbitro_nuevo(request):
    if request.method == "POST":
        formulario = ArbitroForm(request.POST)
        if formulario.is_valid():
            arbitro = formulario.save(commit=False)
            arbitro = Arbitro(nombre = formulario.cleaned_data['nombre'], telefono = formulario.cleaned_data['telefono'])
            arbitro.save()
        return redirect('arbitro_lista')
    else:
        formulario = ArbitroForm()
    return render(request, 'arbitros/arbitro_nuevo.html', {'formulario': formulario})

@login_required
def arbitro_editar(request, pk):
    arbitro = get_object_or_404(Arbitro, pk=pk)
    if request.method == "POST":
        formulario = ArbitroForm(request.POST, instance=arbitro)
        if formulario.is_valid():
            arbitro = formulario.save(commit=False)
            arbitro.save()
        return redirect('arbitro_lista')
    else:
        formulario = ArbitroForm(instance=arbitro)
    return render(request, 'arbitros/arbitro_editar.html', {'formulario': formulario})

@login_required
def arbitro_del(request, pk):
    arbitro = get_object_or_404(Arbitro, pk=pk)
    arbitro.delete()
    return redirect('arbitro_lista')
