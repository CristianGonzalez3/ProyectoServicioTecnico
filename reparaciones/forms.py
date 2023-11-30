# En tu archivo reparaciones/forms.py
from django import forms
from .models import IncidentesXEquipos

class IncidentesXEquiposForm(forms.ModelForm):
    class Meta:
        model = IncidentesXEquipos
        fields = ['descripcion_reparacion', 'fecha_reparacion', 'id_incidente', 'id_equipo']
