from django.urls import path
from reparaciones import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('perfil/', views.perfil, name='perfil'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('perfilusu/', views.perfilusu, name='perfilusu'),
    path('configuracionusu/', views.configuracionusu, name='configuracionusu'),
    
    path('pagina_principal_usuario/', views.pagina_principal_usuario, name='pagina_principal_usuario'),
    path('solicitud/', views.solicitud, name='solicitud'),
    path('reporte/', views.reporte, name='reporte'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('informe/', views.informe, name='informe'),
    
    path('pagina_principal_tecnico/', views.pagina_principal_tecnico, name='pagina_principal_tecnico'),
    path('reparaciones/', views.reparaciones, name='reparaciones'),
    path('reparaciones_agregar/', views.reparaciones_agregar, name='reparaciones_agregar'),
    path('equipos/', views.equipos, name='equipos'),
    path('componentes/', views.componentes, name='componentes'),
    path('componentesN/', views.componentesN, name='componentesN'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('asignaciones/', views.asignaciones, name='asignaciones'),
    

    path('incidentesxequipos/', views.incidentesxequipos_list, name='incidentesxequipos_list'),
    path('incidentesxequipos/<int:pk>/', views.incidentesxequipos_detail, name='incidentesxequipos_detail'),
    path('incidentesxequipos/new/', views.incidentesxequipos_new, name='incidentesxequipos_new'),
    path('incidentesxequipos/<int:pk>/edit/', views.incidentesxequipos_edit, name='incidentesxequipos_edit'),
    path('eliminar_varios_incidentes/', views.eliminar_varios_incidentes, name='eliminar_varios_incidentes'),

    path('enviar_detalle/<int:pk>/<str:correo_destino>/', views.enviar_detalle_por_correo, name='enviar_detalle_por_correo'),
]
