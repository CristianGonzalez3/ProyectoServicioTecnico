# Generated by Django 4.2.7 on 2023-11-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reparaciones', '0013_tecnico_usuario_alter_equiposxusuarios_id_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='descripcion_componente',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='descripcion_equipo',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='equiposxcomponentes',
            name='descripcion_cambio',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='descripcion_incidente',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='incidentesxequipos',
            name='descripcion_reparacion',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='descripcion_solicitud',
            field=models.CharField(max_length=1000),
        ),
    ]
