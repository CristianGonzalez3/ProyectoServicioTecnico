from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

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
    return render(request, 'usuarios/solicitud/solicitud.html', context)

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
    return render(request, 'tecnicos/componentes.html', context)

def solicitudes(request):
    context = {}
    return render(request, 'tecnicos/solicitudes/solicitudes.html', context)

    