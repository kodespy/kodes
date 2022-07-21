import uuid

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

class Marca(ClaseModelo):
	descripcion = models.CharField(
		max_length = 30,
		help_text = 'Descripción de la Marca'
	)

	def __str__(self):
		return '{}'.format(self.descripcion)

	def save(self):
		self.descripcion = self.descripcion.upper()
		super(Marca, self).save()

	class Meta:
		verbose_name_plural = "Marcas"
		unique_together = ('descripcion', 'uc')


class Categoria(ClaseModelo):
	descripcion = models.CharField(
		max_length = 100,
		help_text = 'Descripción de la Categoria'
	)

	def __str__(self):
		return '{}'.format(self.descripcion)

	def save(self):
		self.descripcion = self.descripcion.upper()
		super(Categoria, self).save()

	class Meta:
		verbose_name_plural = "Categorias"		
		unique_together = ('descripcion', 'uc')

class SubCategoria(ClaseModelo):
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	descripcion = models.CharField(
		max_length = 100,
		help_text = 'Descripción de la Sub Categoria'
	)

	def __str__(self):
		return '{} : {}'.format(self.descripcion, self.categoria.descripcion)

	def save(self):
		self.descripcion = self.descripcion.upper()
		super(SubCategoria, self).save()

	class Meta:
		verbose_name_plural = "Sub Categorias"		
		unique_together = ('categoria', 'descripcion', 'uc')



class Proveedor(ClaseModelo):
	documento = models.CharField(
		max_length = 20,
		help_text = 'RUC y/o CI N°'
	)
	razonsocial = models.CharField(
		max_length = 100,
		help_text = 'Razón Social'
	)
	direccion = models.CharField(
		max_length = 200,
		help_text = 'Dirección',
		null=True, blank=True
	)
	contacto = models.CharField(
		max_length = 100,
		help_text = 'Contacto',
	)
	telefono = models.CharField(
		max_length = 20,
		help_text = 'Teléfono',
		null=True, blank=True
	)
	email = models.CharField(
		max_length = 250,
		help_text = 'Teléfono',
		null=True, blank=True
	)
	
	def __str__(self):
		return '{} : {}'.format(self.razonsocial, self.documento)

	def save(self):
		self.razonsocial = self.razonsocial.upper()
		self.direccion = self.direccion.upper()
		self.contacto = self.contacto.upper()
		super(Proveedor, self).save()

	class Meta:
		verbose_name_plural = "Proveedores"	
		unique_together = ('documento', 'uc')


class Producto(ClaseModelo):
	codigo_barra = models.CharField(
		max_length = 50,
		help_text = 'Código de Barra'
	)	
	descripcion = models.CharField(
		max_length = 200,
		help_text = 'Descripción del producto',
	)
	imagen = models.ImageField(
		help_text = 'Imagen',
		upload_to = 'fotos/',
		null = True, blank = True 

	)
	detalle = models.CharField(
		max_length = 250,
		help_text = 'Detalle',
		null = True, blank = True 
	)
	unidad = models.CharField(
		max_length = 3,
		help_text = 'Unidad de Medidas',
	)	
	existencia_inicial = models.FloatField(
		help_text = 'Existencia Inicial',
		default = 0 
	)
	existencia_actual = models.FloatField(
		help_text = 'Existencia Actual',
		default = 0,
		null = True, blank = True 
	)	
	precio_costo = models.FloatField(
		help_text = 'Precio Costo',
		default = 0 
	)
	precio_venta = models.FloatField(
		help_text = 'Precio Venta',
		default = 0 
	)	
	descuento_maximo = models.FloatField(
		help_text = 'Descuentos Máximo',
		default = 0 
	)	
	incremento_precio_credito = models.FloatField(
		help_text = 'Incremento Precio Crédito',
		default = 0 
	)	
	ultima_compra = models.DateField(
		help_text = 'Fecha de Ultima Compra',
		null = True, blank = True
	)	
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
	moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
	subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	IVA = (
       (0, 0),
       (5, 5),
       (10, 10),
   	)
	iva_valor = models.IntegerField(default=10)
	servicio = models.BooleanField(
		help_text = 'Servicios',
		default = False
	)

	def __str__(self):
		return '{}:{}'.format(self.descripcion, self.marca.descripcion)

	def save(self):
		self.descripcion = self.descripcion.upper()
		self.unidad = self.unidad.upper()
		super(Producto, self).save()

	class Meta:
		verbose_name_plural = "Productos"	
		unique_together = ('codigo_barra', 'uc')


class Compras(ClaseModelo):
	id = models.UUIDField(primary_key=True, unique=True, editable=False)
	TIPO = (
       (1, 'Contado'),
       (2, 'Créditos'),
   	)

	factura_numero = models.CharField(
		max_length = 20,
		help_text = 'Factura N°'
	)
	factura_fecha = models.DateField()
	factura_tipo = models.PositiveSmallIntegerField(
       choices=TIPO,default=1)
	factura_total = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	factura_total_iva = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE, related_name="moneda_id")

	def __str__(self):
		return '{}'.format(self.id)

	def save(self):
		#self.razonsocial = self.razonsocial.upper()
		#self.direccion = self.direccion.upper()
		#self.contacto = self.contacto.upper()
		super(Compras, self).save()

	class Meta:
		verbose_name_plural = "Compras"
		unique_together=('factura_numero', 'proveedor_id', 'uc')


class ComprasDetalle(ClaseModelo):
	id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
	IVA = (
       (1, 0),
       (2, 5),
       (3, 10),
   	)
	compras = models.ForeignKey(Compras, on_delete=models.CASCADE, related_name='compras_id')
	producto = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	cantidad = models.DecimalField(default=0, max_digits=6, decimal_places=2)
	iva_valor = models.DecimalField(default=3, choices=IVA, max_digits=4, decimal_places=2)
	precio_costo = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	precio_venta = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	total_iva = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	subtotal = models.DecimalField(default=0, max_digits=12, decimal_places=2)

	def __str__(self):
		return '{}'.format(self.id)

	def save(self):
		#self.razonsocial = self.razonsocial.upper()
		#self.direccion = self.direccion.upper()
		self.subtotal = (self.precio_costo * self.cantidad)
		super(ComprasDetalle, self).save()

	class Meta:
		verbose_name_plural = "ComprasDetalles"	


