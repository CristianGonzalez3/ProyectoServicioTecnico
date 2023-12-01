# En tu archivo reparaciones/forms.py
from django import forms
from .models import IncidentesXEquipos

class IncidentesXEquiposForm(forms.ModelForm):
    class Meta:
        model = IncidentesXEquipos
        fields = ['id_equipo','id_incidente','fecha_reparacion','descripcion_reparacion']
        
    fecha_reparacion = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'datepicker'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y']
    )

class CorreoForm(forms.Form):
    correo_destino = forms.EmailField(label='Correo Electrónico Destino')