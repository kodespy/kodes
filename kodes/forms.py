from django import forms

from .models import Empresa




class EmpresaForm(forms.ModelForm):
	class Meta:
		model = Empresa
		fields = ['documento', 'razonsocial', 'direccion']
		widget = {'razonsocial': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})
		#self.fields['documento'].widget.attrs.update({'class': 'form-control'})	


