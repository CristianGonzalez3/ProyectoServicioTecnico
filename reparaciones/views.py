from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import IncidentesXEquipos
from .forms import IncidentesXEquiposForm
from django.contrib import messages

# Autenticación
def inicio(request):
    query_set = Group.objects.filter(user = request.user)
    for g in query_set:
        if g.name == "Tecnico":
            context = {}
            return render(request, 'inicio/pagina_principal_tecnico.html', context)
        else:
            context = {}
            return render(request, 'inicio/pagina_principal_usuario.html', context)



@login_required
def pagina_principal_usuario(request):
    context = {}
    return render(request, 'inicio/pagina_principal_usuario.html', context)

def perfilusu(request):
    context = {}
    return render(request, 'registration/perfilusu.html', context)


def configuracionusu(request):
    context = {}
    return render(request, 'registration/configuracionusu.html', context)

def solicitud(request):
    context = {}
    return render(request, 'usuarios/solicitud/solicitudd.html', context)

def reporte(request):
    context = {}
    return render(request, 'usuarios/seguimiento/reporte.html', context)

def seguimiento(request):
    context = {}
    return render(request, 'usuarios/seguimiento/seguimiento.html', context)

def informe(request):
    context = {}
    return render(request, 'usuarios/informe/informe.html', context)

@login_required
def pagina_principal_tecnico(request):
    context = {}
    return render(request, 'inicio/pagina_principal_tecnico.html', context)

def perfil(request):
    context = {}
    return render(request, 'registration/perfil.html', context)

def configuracion(request):
    context = {}
    return render(request, 'registration/configuracion.html', context)

def reparaciones(request):
    context = {}
    return render(request, 'tecnicos/reparaciones/reparaciones.html', context)

def reparaciones_agregar(request):
    context = {}
    return render(request, 'tecnicos/reparaciones/reparaciones_agregar.html', context)

def equipos(request):
    context = {}
    return render(request, 'tecnicos/equipos/equipos.html', context)

def componentes(request):
    context = {}
    return render(request, 'tecnicos/componentes/componentes.html', context)

def componentesN(request):
    context = {}
    return render(request, 'tecnicos/componentes/componentesN.html', context)


def solicitudes(request):
    context = {}
    return render(request, 'tecnicos/solicitudes/solicitudes.html', context)

def asignaciones(request):
    context = {}
    return render(request, 'tecnicos/solicitudes/asignaciones.html', context)


# En tu archivo reparaciones/views.py

def incidentesxequipos_list(request):
    incidentesxequipos = IncidentesXEquipos.objects.all()
    return render(request, 'tecnicos/reparaciones/incidentesxequipos_list.html', {'incidentesxequipos': incidentesxequipos})

def incidentesxequipos_detail(request, pk):
    incidentesxequipo = get_object_or_404(IncidentesXEquipos, pk=pk)
    return render(request, 'tecnicos/reparaciones/incidentesxequipos_detail.html', {'incidentesxequipo': incidentesxequipo})

def incidentesxequipos_new(request):
    if request.method == "POST":
        form = IncidentesXEquiposForm(request.POST)
        if form.is_valid():
            incidentesxequipo = form.save(commit=False)
            incidentesxequipo.save()
            return redirect('incidentesxequipos_detail', pk=incidentesxequipo.pk)
    else:
        form = IncidentesXEquiposForm()
    return render(request, 'tecnicos/reparaciones/incidentesxequipos_edit.html', {'form': form})

def incidentesxequipos_edit(request, pk):
    incidentesxequipo = get_object_or_404(IncidentesXEquipos, pk=pk)
    if request.method == "POST":
        form = IncidentesXEquiposForm(request.POST, instance=incidentesxequipo)
        if form.is_valid():
            incidentesxequipo = form.save(commit=False)
            incidentesxequipo.save()
            return redirect('incidentesxequipos_detail', pk=incidentesxequipo.pk)
    else:
        form = IncidentesXEquiposForm(instance=incidentesxequipo)
    return render(request, 'tecnicos/reparaciones/incidentesxequipos_edit.html', {'form': form})

def eliminar_varios_incidentes(request):
    if request.method == 'POST':
        incidentes_a_eliminar = request.POST.getlist('eliminar[]')
        if incidentes_a_eliminar:
            IncidentesXEquipos.objects.filter(pk__in=incidentes_a_eliminar).delete()
            messages.success(request, 'Incidentes eliminados exitosamente.')
        else:
            messages.warning(request, 'Selecciona al menos un incidente para eliminar.')

    return redirect('incidentesxequipos_list')