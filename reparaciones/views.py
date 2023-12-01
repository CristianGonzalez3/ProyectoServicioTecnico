from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import IncidentesXEquipos
from .forms import IncidentesXEquiposForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Autenticación
def inicio(request):
    query_set = Group.objects.filter(user = request.user)
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
    return render(request, 'usuarios/solicitud/solicitud.html', context)

def reporte(request):
    context = {}
    return render(request, 'usuarios/solicitud/reporte.html', context)

def seguimiento(request):
    context = {}
    return render(request, 'usuarios/seguimiento/seguimiento.html', context)

def informe(request):
    context = {}
    return render(request, 'usuarios/informe/informe.html', context)

def solicitudprimera(request):
    context = {}
    return render(request, 'usuarios/solicitud/solicitudprimera.html', context)

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


def enviar_detalle_por_correo(request, pk, correo_destino):
    incidentesxequipo = get_object_or_404(IncidentesXEquipos, pk=pk)

    contenido_html = f"""
        <div>
            <h1>Detalle de Reparaciones</h1>
            <p><strong>Descripción:</strong> {incidentesxequipo.descripcion_reparacion}</p>
            <p><strong>Fecha de Reparación:</strong> {incidentesxequipo.fecha_reparacion}</p>
            <p><strong>Reporte:</strong> {incidentesxequipo.id_incidente}</p>
            <p><strong>Equipo:</strong> {incidentesxequipo.id_equipo}</p>
        </div>
    """

    asunto = 'Detalle de Reparación'
    mensaje = 'Se adjunta el detalle de la reparación en formato HTML.'

    # Dirección de correo electrónico desde la cual enviar
    correo_desde = settings.EMAIL_HOST_USER

    try:
        # Envía el correo con el contenido HTML
        send_mail(asunto, mensaje, correo_desde, [correo_destino], html_message=contenido_html)
        mensaje_respuesta = f'Correo enviado exitosamente a {correo_destino}.'

        # Agrega un mensaje de éxito para mostrar en la página
        messages.success(request, mensaje_respuesta)

        # Redirige a la página de detalles del incidente
        return redirect('incidentesxequipos_detail', pk=pk)
    except Exception as e:
        # Manejar errores
        mensaje_respuesta = f'Error al enviar el correo a {correo_destino}: {str(e)}'
        messages.error(request, mensaje_respuesta)
        return redirect('incidentesxequipos_detail', pk=pk)