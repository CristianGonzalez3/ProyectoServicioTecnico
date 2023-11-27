from django.urls import path
from reparaciones import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('pagina_principal_usuario/', views.pagina_principal_usuario, name='pagina_principal_usuario'),
    path('pagina_principal_tecnico/', views.pagina_principal_tecnico, name='pagina_principal_tecnico'),
    path('pagina_reparaciones/', views.pagina_reparaciones, name='pagina_reparaciones'),
    path('componentesN/', views.componentesN, name='componentesN'),
]
