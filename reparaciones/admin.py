from django.contrib import admin
# # # from django.contrib.auth.models import Permission
from reparaciones.models import Componente, Tecnico, EstadoTecnico, TecnicosXEstados, Usuario, Solicitud, EstadoSolicitud, UsuariosXSolicitudes, Incidente, Equipo, EstadoEquipo, EquiposXUsuarios, EquiposXComponentes, IncidentesXEquipos

admin.site.register(Componente)
admin.site.register(Tecnico)
admin.site.register(EstadoTecnico)
admin.site.register(Usuario)
admin.site.register(Solicitud)
admin.site.register(EstadoSolicitud)
admin.site.register(UsuariosXSolicitudes)
admin.site.register(Incidente)
admin.site.register(Equipo)
admin.site.register(EstadoEquipo)
admin.site.register(EquiposXUsuarios)
admin.site.register(EquiposXComponentes)
admin.site.register(IncidentesXEquipos)
admin.site.register(TecnicosXEstados)