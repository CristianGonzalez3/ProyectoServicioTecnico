from django.db import models
from django.urls import reverse
import uuid

class Componente(models.Model):
    id_componente = models.AutoField(primary_key=True)
    nom_componente = models.CharField(max_length=20)
    descripcion_componente = models.CharField(max_length=1000)
    stock_componente = models.IntegerField()

    def __str__(self):
        return f"{self.nom_componente} - {self.descripcion_componente} - {self.stock_componente}"

class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)
    nom_tecnico = models.CharField(max_length=20)
    apell_tecnico = models.CharField(max_length=20)
    cuil_tecnico = models.BigIntegerField()
    tel_tecnico = models.BigIntegerField()
    dom_tecnico = models.CharField(max_length=50, default='sin domicilio')
    alias_tecnico = models.CharField(max_length=50)
    contra_tecnico = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom_tecnico} - {self.apell_tecnico} - {self.cuil_tecnico} - {self.tel_tecnico} - {self.dom_tecnico} - {self.alias_tecnico} - {self.contra_tecnico}"

class EstadoTecnico(models.Model):
    id_estado_tecnico = models.AutoField(primary_key=True)
    nom_estado_tecnico = models.CharField(max_length=20)

    def __str__(self):
        return  f"{self.nom_estado_tecnico}"

class TecnicosXEstados(models.Model):
    id_tecnicoxestado = models.AutoField(primary_key=True)
    id_tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    id_estado_tecnico = models.ForeignKey(EstadoTecnico, on_delete=models.CASCADE)
    fecha_estado_disponible = models.DateField()

    def get_absolute_url(self):
        return reverse('tecxestInfo', args=[str(self.id)])

    def __str__(self):
        return f'{self.id_tecnico} - {self.id_estado_tecnico} - {self.fecha_estado_disponible}'
    

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nom_usuario = models.CharField(max_length=20)
    apell_usuario = models.CharField(max_length=20)
    cuil_usuario = models.BigIntegerField()
    dom_usuario = models.CharField(max_length=50, default='sin domicilio')
    tel_usuario = models.BigIntegerField()
    alias_usuario = models.CharField(max_length=20)
    contra_usuario = models.CharField(max_length=20)

    def __str__(self):
        return  f"{self.nom_usuario} - {self.apell_usuario}"

class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    descripcion_solicitud = models.CharField(max_length=1000)
    fecha_solicitud = models.DateField()

    def __str__(self):
        return  f"{self.descripcion_solicitud} - {self.fecha_solicitud}"

class EstadoSolicitud(models.Model):
    id_estado_solicitud = models.AutoField(primary_key=True)
    nom_estado_solicitud = models.CharField(max_length=20)

    def __str__(self):
        return  f"{self.nom_estado_solicitud}"

class UsuariosXSolicitudes(models.Model):
    id_usuarioxsolicitud = models.AutoField(primary_key=True)
    id_estado_solicitud = models.ForeignKey(EstadoSolicitud, on_delete=models.CASCADE)
    id_solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_estado_solicitud = models.DateField()

    def get_absolute_url(self):
        return reverse('usuxsolInfo', args=[str(self.id)])

    def __str__(self):
        return f'{self.id_usuario} - {self.fecha_estado_solicitud}'

class Incidente(models.Model):
    id_incidente = models.AutoField(primary_key=True)
    descripcion_incidente = models.CharField(max_length=1000)
    id_usuarioxsolicitud = models.ForeignKey(UsuariosXSolicitudes, on_delete=models.CASCADE)
    id_tecnicoxestado = models.ForeignKey(TecnicosXEstados, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('IncidenteInfo', args=[str(self.id)])

    def __str__(self):
        return f'{self.descripcion_incidente} - {self.id_usuarioxsolicitud}'

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nom_equipo = models.CharField(max_length=30)
    descripcion_equipo = models.CharField(max_length=1000)
    fecha_antiguedad = models.DateField()

    def __str__(self):
        return f"{self.nom_equipo} - {self.descripcion_equipo} - {self.fecha_antiguedad}"

class EstadoEquipo(models.Model):
    id_estado_equipo = models.AutoField(primary_key=True)
    nom_estado_equipo = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_estado_equipo

class EquiposXUsuarios(models.Model):
    id_equipoxusuario = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_estado_equipo = models.ForeignKey(EstadoEquipo, on_delete=models.CASCADE)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_estado_equipo = models.DateField()

    def get_absolute_url(self):
        return reverse('equixusuInfo', args=[str(self.id)])

    def __str__(self):
        return f'{self.id_usuario} - {self.id_estado_equipo} - {self.id_equipo} - {self.fecha_estado_equipo}'

class EquiposXComponentes(models.Model):
    id_equipoxcomponente = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    id_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    descripcion_cambio = models.CharField(max_length=1000)
    fecha_cambio = models.DateField()

    def get_absolute_url(self):
        return reverse('equixcompoInfo', args=[str(self.id)])

    def __str__(self):
        return f'{self.id_equipo} - {self.id_componente} - {self.descripcion_cambio} - {self.fecha_cambio}'

class IncidentesXEquipos(models.Model):
    id_incidentexequipo = models.AutoField(primary_key=True)
    descripcion_reparacion = models.CharField(max_length=1000)
    fecha_reparacion = models.DateField()
    id_incidente = models.ForeignKey(Incidente, on_delete=models.CASCADE)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('incidentexequiInfo', args=[str(self.id)])

    def __str__(self):
        return f'{self.descripcion_reparacion} - {self.fecha_reparacion} - {self.id_incidente} - {self.id_equipo}'
