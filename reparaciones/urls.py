from django.urls import path
from reparaciones import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('pagina_principal_usuario/', views.pagina_principal_usuario, name='pagina_principal_usuario'),
    path('informe/', views.informe, name='informe'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('solicitudd/', views.solicitudd, name='solicitudd'),
    path('perfilusu/', views.perfilusu, name='perfilusu'),
    path('configuracionusu/', views.configuracionusu, name='configuracionusu'),
    path('pagina_principal_tecnico/', views.pagina_principal_tecnico, name='pagina_principal_tecnico'),
    path('pagina_reparaciones/', views.pagina_reparaciones, name='pagina_reparaciones'),
    path('reparaciones_agregar/', views.reparaciones_agregar, name='reparaciones_agregar'),
    path('equipos/', views.equipos, name='equipos'),
    path('componentes/', views.componentes, name='componentes'),
    path('perfil/', views.perfil, name='perfil'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
]
