from django import forms
from .models import Survey, office_division

class demographicsform(forms.ModelForm):
	class Meta:
		model = Survey
		fields = ['office_division_name','presidential_appointee', 'permanent', 'coterminus', 'jo_cos', 'casual_temporary', 'demographics_section']
		widgets = {
			'office_division_name': forms.Select(attrs={'class': 'form-control fieldsize'}),
			'presidential_appointee': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'permanent': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'coterminus': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'jo_cos': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'casual_temporary': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'demographics_section': forms.HiddenInput(attrs={'class': 'form-control fieldsize'}),
		}

	def __init__(self,*args, **kwargs):
		initial_data = kwargs.get('initial', {})
		initial_data['demographics_section'] = 1
		kwargs['initial'] = initial_data
		super().__init__(*args, **kwargs)
		self.fields['office_division_name'].required = True
		self.fields['presidential_appointee'].required = True
		self.fields['permanent'].required = True
		self.fields['coterminus'].required = True
		self.fields['jo_cos'].required = True
		self.fields['casual_temporary'].required = True
		self.fields['demographics_section'].required = True


