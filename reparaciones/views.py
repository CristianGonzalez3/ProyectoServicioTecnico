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
def informe(request):
    context = {}
    return render(request, 'usuario/informe.html', context)
def solicitudd(request):
    context = {}
    return render(request, 'usuario/solicitudd.html', context)
def seguimiento(request):
    context = {}
    return render(request, 'usuario/seguimiento.html', context)
def perfilusu(request):
    context = {}
    return render(request, 'usuario/perfilusu.html', context)
def configuracionusu(request):
    context = {}
    return render(request, 'usuario/configuracionusu.html', context)

@login_required
def pagina_principal_tecnico(request):
    context = {}
    return render(request, 'inicio/pagina_principal_tecnico.html', context)

def pagina_reparaciones(request):
    context = {}
    return render(request, 'tecnicos/reparaciones/pagina_reparaciones.html', context)

def reparaciones_agregar(request):
    context = {}
    return render(request, 'tecnicos/reparaciones/reparaciones_agregar.html', context)

def equipos(request):
    context = {}
    return render(request, 'tecnicos/equipos.html', context)

def componentes(request):
    context = {}
    return render(request, 'tecnicos/componentes.html', context)

def perfil(request):
    context = {}
    return render(request, 'tecnicos/perfil.html', context)

def configuracion(request):
    context = {}
    return render(request, 'tecnicos/configuracion.html', context)

def solicitudes(request):
    context = {}
    return render(request, 'tecnicos/solicitudes.html', context)

    