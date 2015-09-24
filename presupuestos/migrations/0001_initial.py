# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('empresa', models.CharField(max_length=100)),
                ('contacto_nombre', models.CharField(max_length=100)),
                ('contacto_apellido', models.CharField(max_length=100)),
                ('domicilio', models.CharField(max_length=100, blank=b'true')),
                ('telefono_fijo', models.CharField(max_length=100, blank=b'true')),
                ('telefono_movil', models.CharField(max_length=100, blank=b'true')),
                ('email', models.CharField(max_length=100, blank=b'true')),
                ('cuit', models.CharField(max_length=13, blank=b'true')),
                ('nota', models.CharField(max_length=200, blank=b'true')),
            ],
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=100, blank=b'true')),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_de_solicitud', models.DateTimeField(max_length=10)),
                ('fecha_de_aprobacion', models.DateTimeField(max_length=10)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100, blank=b'true')),
                ('observacion', models.CharField(max_length=100, blank=b'true')),
                ('cliente', models.ForeignKey(to='presupuestos.Cliente')),
            ],
        ),
    ]
