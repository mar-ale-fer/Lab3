from django.db import models

class Cliente (models.Model):
	empresa = models.CharField(max_length=100)
	contacto_nombre = models.CharField(max_length=100)
	contacto_apellido = models.CharField(max_length=100)
	domicilio = models.CharField(max_length=100, blank='true')
	telefono_fijo = models.CharField(max_length=100, blank='true')
	telefono_movil = models.CharField(max_length=100, blank='true')
	email = models.CharField(max_length=100, blank='true')
	cuit = models.CharField(max_length=13, blank='true')
	nota = models.CharField(max_length=200, blank='true')
	def __str__(self):
		return self.contacto_apellido+', '+self.contacto_nombre

class Presupuesto (models.Model):
	cliente = models.ForeignKey(Cliente)
	referencia = models.CharField(max_length=100, blank='true')
	tipo = models.CharField(max_length=100)
	fecha_de_solicitud = models.DateTimeField(max_length=10)
	fecha_de_aprobacion = models.DateTimeField(max_length=10)
	#fecha_de_solicitud = models.DateTimeField('')
	#fecha_de_aprobacion = models.DateTimeField('')
	descripcion = models.CharField(max_length=100)
	estado = models.CharField(max_length=100, blank='true')
	observacion = models.CharField(max_length=100, blank='true')
	"""def __str__(self):
		return self.fecha_de_solicitud"""
	def __str__(self):
		return self.cliente

