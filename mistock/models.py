from django.db import models
from django.core.validators import RegexValidator

from kodes.models import ClaseModelo

numerico = RegexValidator(r'^[0-9+]', 'Only digit characters.')

class Moneda(ClaseModelo):
	descripcion = models.CharField(
		max_length = 30,
		help_text = 'Descripción de la Marca'
	)
	simbolo = models.CharField(
		max_length = 3,
		help_text = 'Simbolo de la Moneda'
	)
	compras = models.IntegerField(
		help_text = 'Valor de compras',
		default = 0,
		validators=[numerico] 
	)
	ventas = models.IntegerField(
		help_text = 'Valor de ventas',
		default = 0, 
		validators=[numerico] 
	)
	maestra = models.BooleanField(
		help_text = 'Moneda Maestra',
		default = False
	)

	def __str__(self):
		return '{} : {}'.format(self.descripcion, self.simbolo)

	def save(self):
		self.descripcion = self.descripcion.upper()
		self.simbolo = self.simbolo.upper()
		super(Moneda, self).save()

	class Meta:
		verbose_name_plural = "Monedas"	
		unique_together = ('descripcion', 'uc')
		unique_together = ('simbolo', 'uc')
