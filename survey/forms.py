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

		labels = {
			'office_division_name': 'Office/Divison Name',
			'presidential_appointee': 'Number of Presidential Appointees',
			'permanent': 'Number of Permanent Employees',
			'coterminus': 'Number of Coterminous Employees',
			'jo_cos': 'Number of Job Order/Contract of Service Employees',
			'casual_temporary': 'Number of Casual/Temporary Employees',
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

class hardwareform(forms.ModelForm):
	class Meta:
		model = Survey
		fields = ['desktop_acer_installed', 'desktop_hp_installed', 'desktop_lenovo_installed', 'desktop_samsung_installed',
		 'hardware_section', 'laptop_acer_installed', 'laptop_hp_installed', 'laptop_lenovo_installed', 'laptop_samsung_installed']
		widgets = {
			'desktop_acer_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'desktop_hp_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'desktop_lenovo_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'desktop_samsung_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'hardware_section': forms.HiddenInput(attrs={'class': 'form-control fieldsize'}),

			'laptop_acer_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'laptop_hp_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'laptop_lenovo_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'laptop_samsung_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
		}
		labels = {
			'desktop_acer_installed': 'Acer',
			'desktop_hp_installed': 'HP',
			'desktop_lenovo_installed': 'Lenovo',
			'desktop_samsung_installed': 'Samsung',

			'laptop_acer_installed': 'Acer',
			'laptop_hp_installed': 'HP',
			'laptop_lenovo_installed': 'Lenovo',
			'laptop_samsung_installed': 'Samsung',
		}
	def __init__(self,*args, **kwargs):
		initial_data = kwargs.get('initial', {})
		initial_data['hardware_section'] = 1
		kwargs['initial'] = initial_data
		super().__init__(*args, **kwargs)

