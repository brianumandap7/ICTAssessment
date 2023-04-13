from django import forms
from .models import Survey, office_division

class demographicsform(forms.ModelForm):
	class Meta:
		model = Survey
		fields = ['office_division_name','presidential_appointee', 'permanent', 'coterminus', 'jo_cos', 'casual_temporary', 'male',
		 'female', 'age_20_24', 'age_25_34', 'age_35_44', 'age_45_54', 'age_55_above', 'demographics_section']
		widgets = {
			'office_division_name': forms.Select(attrs={'class': 'form-control fieldsize'}),
			'presidential_appointee': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'permanent': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'coterminus': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'jo_cos': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'casual_temporary': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'male': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'female': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'age_20_24': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'age_25_34': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'age_35_44': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'age_45_54': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'age_55_above': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'demographics_section': forms.HiddenInput(attrs={'class': 'form-control fieldsize'}),
		}

		labels = {
			'office_division_name': 'Office/Divison Name',
			'presidential_appointee': 'Number of Presidential Appointees',
			'permanent': 'Number of Permanent Employees',
			'coterminus': 'Number of Coterminous Employees',
			'jo_cos': 'Number of JO/COS Employees',
			'casual_temporary': 'Number of Casual/Temporary Employees',
			'male': 'Number of Male Personnel',
			'female': 'Number of Female Personnel',
			'age_20_24': 'Age 20-24',
			'age_25_34': 'Age 25-34',
			'age_35_44': 'Age 35-44',
			'age_45_54': 'Age 45-54',
			'age_55_above': 'Age 55 and Above',
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
		self.fields['male'].required = True
		self.fields['female'].required = True
		self.fields['age_20_24'].required = True
		self.fields['age_25_34'].required = True
		self.fields['age_35_44'].required = True
		self.fields['age_45_54'].required = True
		self.fields['age_55_above'].required = True
		self.fields['demographics_section'].required = True


class hardwareform(forms.ModelForm):
	class Meta:
		model = Survey
		fields = ['desktop_acer_installed', 'desktop_hp_installed', 'desktop_lenovo_installed', 'desktop_samsung_installed',
		 'hardware_section', 'laptop_acer_installed', 'laptop_hp_installed', 'laptop_lenovo_installed', 'laptop_samsung_installed',
		 'desktop_personal', 'laptop_personal', 'tablet_office', 'tablet_personal', 'mouse_office', 'mouse_personal',
		 'keyboard_office', 'keyboard_personal', 'monitor_office', 'monitor_personal',
		 'ordinaryprinter_shared', 'coloredprinter_shared', 'scanner_shared', 'speaker_shared', 'tv_shared',
		 'projector_shared', 'camera_shared', 'microphone_shared', 'photocopier_shared',
		 'ordinaryprinter_shared_personal', 'coloredprinter_shared_personal', 'scanner_shared_personal',
		 'speaker_shared_personal', 'tv_shared_personal',
		 'projector_shared_personal', 'camera_shared_personal', 'microphone_shared_personal', 'photocopier_shared_personal',
		 'desktop_need', 'laptop_need', 'tablet_need', 'mouse_need', 'keyboard_need', 'monitor_need',
		 'ordinaryprinter_need', 'coloredprinter_need', 'scanner_need', 'speaker_need', 'tv_need',
		 'projector_need', 'camera_need', 'microphone_need', 'photocopier_need', 'hardware_comments']
		
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
			'desktop_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'laptop_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'tablet_office': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'tablet_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'mouse_office': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'mouse_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'keyboard_office': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'keyboard_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'monitor_office': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'monitor_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'ordinaryprinter_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'coloredprinter_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'scanner_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'speaker_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'tv_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'projector_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'camera_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'microphone_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'photocopier_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'ordinaryprinter_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'coloredprinter_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'scanner_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'speaker_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'tv_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'projector_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'camera_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'microphone_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'photocopier_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'desktop_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'laptop_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'tablet_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'mouse_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'keyboard_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'monitor_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'ordinaryprinter_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'coloredprinter_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'scanner_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'speaker_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'tv_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'projector_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'camera_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'microphone_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'photocopier_need': forms.NumberInput(attrs={'class': 'form-control fieldsize'}),
			'hardware_comments': forms.Textarea(attrs={'class': 'form-control'}),
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
		self.fields['desktop_acer_installed'].required = True
		self.fields['desktop_hp_installed'].required = True
		self.fields['desktop_lenovo_installed'].required = True
		self.fields['desktop_samsung_installed'].required = True
		self.fields['laptop_acer_installed'].required = True
		self.fields['laptop_hp_installed'].required = True
		self.fields['laptop_lenovo_installed'].required = True
		self.fields['laptop_samsung_installed'].required = True
		self.fields['desktop_personal'].required = True
		self.fields['laptop_personal'].required = True
		self.fields['tablet_office'].required = True
		self.fields['tablet_personal'].required = True
		self.fields['mouse_office'].required = True
		self.fields['mouse_personal'].required = True
		self.fields['keyboard_office'].required = True
		self.fields['keyboard_personal'].required = True
		self.fields['monitor_office'].required = True
		self.fields['monitor_personal'].required = True
		self.fields['ordinaryprinter_shared'].required = True
		self.fields['coloredprinter_shared'].required = True
		self.fields['scanner_shared'].required = True
		self.fields['speaker_shared'].required = True
		self.fields['tv_shared'].required = True
		self.fields['projector_shared'].required = True
		self.fields['camera_shared'].required = True
		self.fields['microphone_shared'].required = True
		self.fields['photocopier_shared'].required = True
		self.fields['ordinaryprinter_shared_personal'].required = True
		self.fields['coloredprinter_shared_personal'].required = True
		self.fields['scanner_shared_personal'].required = True
		self.fields['speaker_shared_personal'].required = True
		self.fields['tv_shared_personal'].required = True
		self.fields['projector_shared_personal'].required = True
		self.fields['camera_shared_personal'].required = True
		self.fields['microphone_shared_personal'].required = True
		self.fields['photocopier_shared_personal'].required = True
		self.fields['hardware_comments'].required = True



