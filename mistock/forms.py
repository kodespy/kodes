from time import gmtime, strftime


from django import forms

from .models import Moneda, Marca, Categoria, SubCategoria, \
	Proveedor, Producto, Compras 
from kodes.models import Usuario

class MonedaForm(forms.ModelForm):
	class Meta:
		model = Moneda
		fields = ['descripcion', 'simbolo', 'compras', 'ventas', 'maestra']
		labels = {'descripcion': "Descripción de la Moneda", 'simbolo': "simbolo de la moneda",
			'compras': 'Valor de Compras', 'ventas': 'Valor de Ventas', 'maestra': 'Si es moneda maestra'}
		widget = {'descripcion': forms.TextInput}
		compras = forms.IntegerField(min_value=1, 
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
		ventas = forms.IntegerField(min_value=1, 
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})
		self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})	
		self.fields['descripcion'].empty_label = "Descripción de la Moneda"
		self.fields['simbolo'].empty_label = "Simbolo de la Moneda"



class MarcaForm(forms.ModelForm):
	class Meta:
		model = Marca
		fields = ['descripcion']
		labels = {'descripcion': "Descripción de la Marca"}
		widget = {'descripcion': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})			

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = ['descripcion']
		labels = {'descripcion': "Descripción de la Categoria"}
		widget = {'descripcion': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})			

class SubCategoriaForm(forms.ModelForm):
	categoria = forms.ModelChoiceField(
		queryset=Categoria.objects.filter(estado=True)
		.order_by('descripcion')
	)
	class Meta:
		model = SubCategoria
		fields = [ 'descripcion', 'categoria']
		labels = {'descripcion': "Descripción de la Sub Categoria"}
		widget = {'descripcion': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})
		self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})	
		self.fields['descripcion'].empty_label = "Descripción de la Categoria"
		self.fields['categoria'].empty_label = "Seleccionar Categoria"				


class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = ['documento', 'razonsocial', 'direccion','contacto', 
			'telefono', 'email']
		labels = {'documento': "RUC y/o CI N°", 'razonsocial': "Razón Social", 
			'direccion': "Dirección", 'contacto': "Contacto", 
			'telefono': "Teléfono", 'email': "Email"}
		widget = {'documento': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})	
		self.fields['documento'].widget.attrs.update({'class': 'form-control'})	
		self.fields['razonsocial'].empty_label = "Razón Social"
		self.fields['direccion'].empty_label = "Dirección"

class ProductoForm(forms.ModelForm):
	detalle = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))	

	class Meta:
		model = Producto
		fields = ['codigo_barra', 'descripcion', 'unidad', 'existencia_inicial',
			'existencia_actual', 'precio_costo', 'precio_venta', 'descuento_maximo',
			'incremento_precio_credito', 'ultima_compra', 'subcategoria', 'marca',
			'moneda', 'proveedor', 'imagen', 'detalle', 'iva_valor', 'servicio']
		labels = {'descripcion': "Descripción del Producto"}
		widget = {'descripcion': forms.TextInput}

	
	def __init__(self, *args,  **kwargs):
		user = kwargs.pop('user')
		existencia = kwargs.pop('existencia')
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})
		self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})	
		self.fields['descripcion'].empty_label = "Descripción del producto"
		self.fields['subcategoria'].empty_label = "Seleccionar Sub Categoria"			
		self.fields['marca'].empty_label = "Seleccionar Marca"					
		self.fields['moneda'].empty_label = "Seleccionar Moneda"							
		self.fields['proveedor'].empty_label = "Seleccionar Proveedor"	
		self.fields['iva_valor'].empty_label = "Seleccionar Valor de Iva"	
		self.fields['precio_costo'].widget.attrs['class'] = "form-control"
		self.fields['precio_venta'].widget.attrs['class'] = "form-control"
		self.fields['descuento_maximo'].widget.attrs['class'] = "form-control"
		self.fields['incremento_precio_credito'].widget.attrs['class'] = "form-control"
		self.fields['existencia_actual'].widget.attrs['class'] = "form-control"
		self.fields['existencia_inicial'].widget.attrs['class'] = "form-control"
		empresa = user.empresa.id
		self.fields['moneda'].queryset = Moneda.objects.order_by('descripcion').filter(estado=True, uc_id=empresa)
		self.fields['subcategoria'].queryset = SubCategoria.objects.order_by('descripcion').filter(estado=True, uc_id=empresa)		
		self.fields['proveedor'].queryset = Proveedor.objects.order_by('razonsocial').filter(estado=True, uc_id=empresa)		
		self.fields['marca'].queryset = Marca.objects.order_by('descripcion').filter(estado=True, uc_id=empresa)				
		if (existencia > 0):
			self.fields['existencia_inicial'].widget.attrs['readonly'] = True

		
class ComprarForm(forms.ModelForm):
	class Meta:
		model = Compras
		fields = ['factura_numero', 'factura_fecha', 'factura_tipo', 
		'proveedor', 'moneda', 'factura_total']
		labels = {'factura_numero': "N° de Factura"}
		widget = {'factura_numero': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		user = kwargs.pop('user')
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})
		empresa = user.empresa.id					
		self.fields['proveedor'].queryset = Proveedor.objects.order_by('razonsocial').filter(estado=True, uc_id=empresa)			
		self.fields['proveedor'].empty_label = "Seleccionar Proveedor"
		self.fields['moneda'].queryset = Moneda.objects.order_by('descripcion').filter(estado=True, uc_id=empresa)		
		self.fields['moneda'].empty_label = "Seleccionar Moneda"								
		self.fields['factura_fecha'].widget.attrs.update({'autofocus': 'True'})
		self.fields['factura_total'].widget.attrs['readonly'] = True
		self.fields['factura_total'].widget.attrs.update({'style': 'text-align:right; color:green;'})
		self.fields['factura_total'].initial = 0
		fecha = strftime("%d-%m-%Y", gmtime())
		self.fields['factura_fecha'].initial = fecha




