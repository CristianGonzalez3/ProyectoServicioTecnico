# Generated by Django 4.2.7 on 2023-11-27 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reparaciones', '0011_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id_componente', models.AutoField(primary_key=True, serialize=False)),
                ('nom_componente', models.CharField(max_length=20)),
                ('descripcion_componente', models.CharField(max_length=100)),
                ('stock_componente', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nom_equipo', models.CharField(max_length=30)),
                ('descripcion_equipo', models.CharField(max_length=100)),
                ('fecha_antiguedad', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EstadoEquipo',
            fields=[
                ('id_estado_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nom_estado_equipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoSolicitud',
            fields=[
                ('id_estado_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('nom_estado_solicitud', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoTecnico',
            fields=[
                ('id_estado_tecnico', models.AutoField(primary_key=True, serialize=False)),
                ('nom_estado_tecnico', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('id_incidente', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_incidente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_solicitud', models.CharField(max_length=100)),
                ('fecha_solicitud', models.DateField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='cuil',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.CreateModel(
            name='UsuariosXSolicitudes',
            fields=[
                ('id_usuarioxsolicitud', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_estado_solicitud', models.DateField()),
                ('id_estado_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.estadosolicitud')),
                ('id_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.solicitud')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.user')),
            ],
        ),
        migrations.CreateModel(
            name='TecnicosXEstados',
            fields=[
                ('id_tecnicoxestado', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_estado_disponible', models.DateField()),
                ('id_estado_tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.estadotecnico')),
                ('id_tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.user')),
            ],
        ),
        migrations.CreateModel(
            name='IncidentesXEquipos',
            fields=[
                ('id_incidentexequipo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_reparacion', models.CharField(max_length=50)),
                ('fecha_reparacion', models.DateField()),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.equipo')),
                ('id_incidente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.incidente')),
            ],
        ),
        migrations.AddField(
            model_name='incidente',
            name='id_tecnicoxestado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.tecnicosxestados'),
        ),
        migrations.AddField(
            model_name='incidente',
            name='id_usuarioxsolicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.usuariosxsolicitudes'),
        ),
        migrations.CreateModel(
            name='EquiposXUsuarios',
            fields=[
                ('id_equipoxusuario', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_estado_equipo', models.DateField()),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.equipo')),
                ('id_estado_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.estadoequipo')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.user')),
            ],
        ),
        migrations.CreateModel(
            name='EquiposXComponentes',
            fields=[
                ('id_equipoxcomponente', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_cambio', models.CharField(max_length=100)),
                ('fecha_cambio', models.DateField()),
                ('id_componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.componente')),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.equipo')),
            ],
        ),
    ]