# Generated by Django 4.2.7 on 2023-11-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reparaciones', '0002_remove_tecnico_tipo_remove_usuario_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tecnico',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='tecnico',
            name='password',
            field=models.CharField(default=2, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='contra_tecnico',
            field=models.CharField(default='password1', max_length=50),
        ),
    ]
