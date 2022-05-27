from django import forms

from .models import Moneda

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
		#self.fields['compras'].widget.attrs['class'] = "text_type_number"
		#self.fields['ventas'].widget.attrs['class'] = "text_type_number"


