from django import forms
from .models import IncidentesXEquipos

class IncidentesXEquiposForm(forms.ModelForm):
    class Meta:
        model = IncidentesXEquipos
        fields = ['id_equipo','id_incidente','fecha_reparacion','descripcion_reparacion']
        
