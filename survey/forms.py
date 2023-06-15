from django import forms
from .models import Survey, ProfessionalToolsOption, CompetencyScale, ICTTrainingPrograms, CommunicationToolsOption, ProductivityOption, StorageOption, OnlineStorageOption, BackupStorageOption, OnlineOption, OfficeLocation, ConnectionOption
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError

def validate_check_at_least_one(value):
    if not value:
        raise ValidationError("Please select at least one option for the questions containing checkboxes.")

class demographicsform(forms.ModelForm):
	office_location = forms.ModelMultipleChoiceField(queryset=OfficeLocation.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}), validators=[validate_check_at_least_one])
	pmo_office = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield pmos form-control'}))
	office_location_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield form-control'}))
	class Meta:
		model = Survey
		fields = ['office_division_name','presidential_appointee', 'permanent', 'coterminus', 'jo_cos', 'casual_temporary', 'male',
		 'female', 'age_20_24', 'age_25_34', 'age_35_44', 'age_45_54', 'age_55_above', 'demographics_section', 'office_location', 'pmo_office', 'office_location_others']
		widgets = {
			'office_division_name': forms.Select(attrs={'class': 'form-control fieldsize'}),
			'presidential_appointee': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'permanent': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'coterminus': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'jo_cos': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'casual_temporary': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'male': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'female': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'age_20_24': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'age_25_34': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'age_35_44': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'age_45_54': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'age_55_above': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'min': '0', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'demographics_section': forms.HiddenInput(attrs={'class': 'form-control fieldsize'}),
		}

		labels = {
			'office_division_name': 'Office/Division Name',
			'presidential_appointee': 'Number of Presidential Appointees',
			'permanent': 'Number of Permanent Employees',
			'coterminus': 'Number of Co-terminous Employees',
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
	connection_option = forms.ModelMultipleChoiceField(queryset=ConnectionOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
	class Meta:
		model = Survey
		fields = ['desktop_acer_installed', 'desktop_hp_installed', 'desktop_lenovo_installed', 'desktop_samsung_installed',
		 'desktop_others_installed',
		 'hardware_section', 'laptop_acer_installed', 'laptop_hp_installed', 'laptop_lenovo_installed', 'laptop_samsung_installed',
		 'laptop_others_installed',
		 'desktop_acer_personal', 'desktop_hp_personal', 'desktop_lenovo_personal', 'desktop_samsung_personal', 'desktop_others_personal',
		 'laptop_acer_personal', 'laptop_hp_personal', 'laptop_lenovo_personal', 'laptop_samsung_personal', 'laptop_others_personal',
		 'tablet_acer_installed', 'tablet_hp_installed', 'tablet_lenovo_installed', 'tablet_samsung_installed', 'tablet_others_installed',
		 'tablet_acer_personal', 'tablet_hp_personal', 'tablet_lenovo_personal', 'tablet_samsung_personal', 'tablet_others_personal',
		 'mouse_acer_installed', 'mouse_hp_installed', 'mouse_lenovo_installed', 'mouse_samsung_installed', 'mouse_others_installed',
		 'mouse_acer_personal', 'mouse_hp_personal', 'mouse_lenovo_personal', 'mouse_samsung_personal', 'mouse_others_personal',
		 'kb_acer_installed', 'kb_hp_installed', 'kb_lenovo_installed', 'kb_samsung_installed', 'kb_others_installed',
		 'kb_acer_personal', 'kb_hp_personal', 'kb_lenovo_personal', 'kb_samsung_personal', 'kb_others_personal',
		 'monitor_acer_installed', 'monitor_hp_installed', 'monitor_lenovo_installed', 'monitor_samsung_installed', 'monitor_others_installed',
		 'monitor_acer_personal', 'monitor_hp_personal', 'monitor_lenovo_personal', 'monitor_samsung_personal', 'monitor_others_personal',
		 'ordinaryprinter_shared', 'coloredprinter_shared', 'scanner_shared', 'speaker_shared', 'tv_shared',
		 'projector_shared', 'camera_shared', 'microphone_shared', 'photocopier_shared',
		 'ordinaryprinter_shared_personal', 'coloredprinter_shared_personal', 'scanner_shared_personal',
		 'speaker_shared_personal', 'tv_shared_personal',
		 'projector_shared_personal', 'camera_shared_personal', 'microphone_shared_personal', 'photocopier_shared_personal',
		 'desktop_need', 'laptop_need', 'tablet_need', 'mouse_need', 'keyboard_need', 'monitor_need',
		 'ordinaryprinter_need', 'coloredprinter_need', 'scanner_need', 'speaker_need', 'tv_need',
		 'projector_need', 'camera_need', 'microphone_need', 'photocopier_need', 'hardware_comments', 'connection_option']
		
		widgets = {
			'desktop_acer_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'desktop_hp_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'desktop_lenovo_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'desktop_samsung_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'desktop_others_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'hardware_section': forms.HiddenInput(attrs={'class': 'form-control fieldsize'}),
			'laptop_acer_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'laptop_hp_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'laptop_lenovo_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize','oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'laptop_samsung_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'laptop_others_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'desktop_acer_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'desktop_hp_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'desktop_lenovo_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'desktop_samsung_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'desktop_others_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'laptop_acer_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'laptop_hp_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'laptop_lenovo_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'laptop_samsung_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'laptop_others_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tablet_acer_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tablet_hp_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tablet_lenovo_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tablet_samsung_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tablet_others_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tablet_acer_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tablet_hp_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tablet_lenovo_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tablet_samsung_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tablet_others_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),

			'mouse_acer_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'mouse_hp_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'mouse_lenovo_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'mouse_samsung_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'mouse_others_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),

			'mouse_acer_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'mouse_hp_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'mouse_lenovo_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'mouse_samsung_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'mouse_others_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),

			'kb_acer_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'kb_hp_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'kb_lenovo_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'kb_samsung_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'kb_others_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),

			'kb_acer_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'kb_hp_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'kb_lenovo_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'kb_samsung_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'kb_others_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),

			'monitor_acer_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'monitor_hp_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'monitor_lenovo_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'monitor_samsung_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'monitor_others_installed': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),

			'monitor_acer_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'monitor_hp_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'monitor_lenovo_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'monitor_samsung_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'monitor_others_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),

			'ordinaryprinter_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'coloredprinter_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'scanner_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'speaker_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tv_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'projector_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'camera_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'microphone_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'photocopier_shared': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'ordinaryprinter_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'coloredprinter_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'scanner_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'speaker_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tv_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'projector_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'camera_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'microphone_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'photocopier_shared_personal': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'desktop_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'laptop_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tablet_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'mouse_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'keyboard_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'monitor_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'ordinaryprinter_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'coloredprinter_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'scanner_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'speaker_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'tv_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'projector_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'camera_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'microphone_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'photocopier_need': forms.NumberInput(attrs={'class': 'form-control fieldsize', 'oninput': "this.value = this.value.replace(/^[-]/, '')"}),
			'hardware_comments': forms.Textarea(attrs={'class': 'form-control'}),
		}
		labels = {
			'desktop_acer_installed': 'Acer',
			'desktop_hp_installed': 'HP',
			'desktop_lenovo_installed': 'Lenovo',
			'desktop_samsung_installed': 'Samsung',
			'desktop_others_installed': 'Others',

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
		self.fields['desktop_others_installed'].required = True
		self.fields['laptop_acer_installed'].required = True
		self.fields['laptop_hp_installed'].required = True
		self.fields['laptop_lenovo_installed'].required = True
		self.fields['laptop_samsung_installed'].required = True
		self.fields['laptop_others_installed'].required = True
		self.fields['tablet_acer_installed'].required = True
		self.fields['tablet_hp_installed'].required = True
		self.fields['tablet_lenovo_installed'].required = True
		self.fields['tablet_samsung_installed'].required = True
		self.fields['tablet_others_installed'].required = True
		self.fields['mouse_acer_installed'].required = True
		self.fields['mouse_hp_installed'].required = True
		self.fields['mouse_lenovo_installed'].required = True
		self.fields['mouse_samsung_installed'].required = True
		self.fields['mouse_others_installed'].required = True
		self.fields['kb_acer_installed'].required = True
		self.fields['kb_hp_installed'].required = True
		self.fields['kb_lenovo_installed'].required = True
		self.fields['kb_samsung_installed'].required = True
		self.fields['kb_others_installed'].required = True
		self.fields['monitor_acer_installed'].required = True
		self.fields['monitor_hp_installed'].required = True
		self.fields['monitor_lenovo_installed'].required = True
		self.fields['monitor_samsung_installed'].required = True
		self.fields['monitor_others_installed'].required = True
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
		self.fields['desktop_need'].required = True
		self.fields['laptop_need'].required = True
		self.fields['tablet_need'].required = True
		self.fields['mouse_need'].required = True
		self.fields['keyboard_need'].required = True
		self.fields['monitor_need'].required = True
		self.fields['ordinaryprinter_need'].required = True
		self.fields['coloredprinter_need'].required = True
		self.fields['scanner_need'].required = True
		self.fields['speaker_need'].required = True
		self.fields['tv_need'].required = True
		self.fields['projector_need'].required = True
		self.fields['camera_need'].required = True
		self.fields['microphone_need'].required = True
		self.fields['photocopier_need'].required = True
		self.fields['hardware_comments'].required = True

class SoftwareForm(forms.ModelForm):
    dotr_issued_professional_tools_installed = forms.ModelMultipleChoiceField(queryset=ProfessionalToolsOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    personal_owned_professional_tools_installed = forms.ModelMultipleChoiceField(queryset=ProfessionalToolsOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    professional_tools_needed = forms.ModelMultipleChoiceField(queryset=ProfessionalToolsOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    communication_tools_installed = forms.ModelMultipleChoiceField(queryset=CommunicationToolsOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    communication_tools_needed = forms.ModelMultipleChoiceField(queryset=CommunicationToolsOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    communication_tools_installed_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
    communication_tools_needed_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
    dotr_issued_professional_tools_installed_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
    personal_owned_professional_tools_installed_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
    professional_tools_needed_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
    dotr_issued_productivity_installed = forms.ModelMultipleChoiceField(queryset=ProductivityOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    dotr_issued_productivity_installed_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
    personal_owned_productivity_installed = forms.ModelMultipleChoiceField(queryset=ProductivityOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    personal_owned_productivity_installed_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
    productivity_needed = forms.ModelMultipleChoiceField(queryset=ProductivityOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    productivity_needed_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))

    professional_frequent = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control fm'}))
    professional_most_needed = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control fm'}))
    communication_frequent = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control fm'}))
    communication_most_needed = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control fm'}))
    productivity_frequent = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control fm'}))
    productivity_most_needed = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control fm'}))

    class Meta:
        model = Survey
        fields = ['dotr_issued_professional_tools_installed', 'personal_owned_professional_tools_installed', 'professional_tools_needed', 'software_section',
        'communication_tools_installed', 'communication_tools_needed',
        'communication_tools_installed_others', 'communication_tools_needed_others',
        'dotr_issued_professional_tools_installed_others', 'personal_owned_professional_tools_installed_others',
        'professional_tools_needed_others',
        'dotr_issued_productivity_installed', 'dotr_issued_productivity_installed_others',
        'personal_owned_productivity_installed', 'personal_owned_productivity_installed_others', 'productivity_needed', 'productivity_needed_others',
        'software_comments', 'professional_frequent', 'professional_most_needed', 'communication_frequent', 'communication_most_needed',
        'productivity_frequent', 'productivity_most_needed']
        
        widgets = {
			'software_section': forms.HiddenInput(attrs={'class': 'form-control fieldsize'}),
			'software_comments': forms.Textarea(attrs={'class': 'form-control'}),
		}
    def __init__(self,*args, **kwargs):
    	initial_data = kwargs.get('initial', {})
    	initial_data['software_section'] = 1
    	kwargs['initial'] = initial_data
    	super(SoftwareForm, self).__init__(*args, **kwargs)
    	self.helper = FormHelper(self)
    	self.helper.form_show_labels = False
    	self.fields['software_comments'].required = True
    	


class CompetenciesForm(forms.ModelForm):

    turning_on_familiar  = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'required': False}))
    network_cable_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    network_wifi_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    usb_printer_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    wireless_printer_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    saving_files_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    creating_folders_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    copying_deleting_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    installing_software = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    file_types_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    unzip_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    file_search_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    connect_device_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    
    access_email_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    sending_email_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    add_attachments_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    add_signatures_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    mailing_list_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    
    gmail_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    meet_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    calendar_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    drive_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    docs_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    sheets_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    sliders_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    forms_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    sites_familiar= forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    keep_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

    outlook_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    teams_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    onedrive_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    word_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    excel_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    ppt_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    forms2_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    sharepoint_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    onenote_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    powerbi_familiar = forms.ModelChoiceField(queryset=CompetencyScale.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

    online_options = forms.ModelChoiceField(queryset=OnlineOption.objects.all(), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Survey
        fields = ['turning_on_familiar', 'network_cable_familiar', 'network_wifi_familiar', 'usb_printer_familiar',
        'wireless_printer_familiar', 'saving_files_familiar', 'creating_folders_familiar', 'copying_deleting_familiar',
        'installing_software', 'file_types_familiar', 'unzip_familiar', 'file_search_familiar', 'connect_device_familiar',
        'gmail_familiar', 'meet_familiar', 'calendar_familiar', 'competencies_section', 'competencies_comments',
        'access_email_familiar', 'sending_email_familiar', 'add_attachments_familiar', 'add_signatures_familiar',
        'mailing_list_familiar',
        'drive_familiar', 'docs_familiar', 'sheets_familiar', 'sliders_familiar', 'forms_familiar',
        'sites_familiar', 'keep_familiar',
        'outlook_familiar', 'teams_familiar', 'onedrive_familiar', 'word_familiar', 'excel_familiar',
        'ppt_familiar', 'forms2_familiar', 'sharepoint_familiar', 'onenote_familiar', 'powerbi_familiar', 'online_options',]

        widgets = {
			'competencies_section': forms.HiddenInput(attrs={'class': 'form-control fieldsize'}),
			'competencies_comments': forms.Textarea(attrs={'class': 'form-control'}),
		}
    def __init__(self,*args, **kwargs):
    	initial_data = kwargs.get('initial', {})
    	initial_data['competencies_section'] = 1
    	kwargs['initial'] = initial_data
    	super(CompetenciesForm, self).__init__(*args, **kwargs)
    	self.helper = FormHelper(self)
    	self.helper.form_show_labels = False
		

class ICTTrainingsForm(forms.ModelForm):
    ict_trainings_taken = forms.ModelMultipleChoiceField(queryset=ICTTrainingPrograms.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    ict_trainings_interests = forms.ModelMultipleChoiceField(queryset=ICTTrainingPrograms.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    ict_trainings_taken_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
    ict_trainings_interests_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
    class Meta:
        model = Survey
        fields = ['ict_trainings_taken', 'ict_trainings_interests', 'ict_trainings_taken_others',
        'ict_trainings_interests_others', 'ict_training_comments', 'trainings_section']

        widgets = {
			'trainings_section': forms.HiddenInput(attrs={'class': 'form-control fieldsize'}),
			'ict_training_comments': forms.Textarea(attrs={'class': 'form-control'}),
		}
	
    def __init__(self,*args, **kwargs):
    	initial_data = kwargs.get('initial', {})
    	initial_data['trainings_section'] = 1
    	kwargs['initial'] = initial_data
    	super(ICTTrainingsForm, self).__init__(*args, **kwargs)
    	self.helper = FormHelper(self)
    	self.helper.form_show_labels = False


class StorageForm(forms.ModelForm):
	dotr_storage = forms.ModelMultipleChoiceField(queryset=StorageOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
	personal_storage = forms.ModelMultipleChoiceField(queryset=StorageOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
	dotr_storage_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
	personal_storage_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
	storage_need = forms.ModelMultipleChoiceField(queryset=StorageOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
	storage_need_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
	dotr_online_storage = forms.ModelMultipleChoiceField(queryset=OnlineStorageOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
	personal_online_storage = forms.ModelMultipleChoiceField(queryset=OnlineStorageOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
	online_storage_need = forms.ModelMultipleChoiceField(queryset=OnlineStorageOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
	backup_storage = forms.ModelMultipleChoiceField(queryset=BackupStorageOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
	backup_storage_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))
	backup_storage_need = forms.ModelMultipleChoiceField(queryset=BackupStorageOption.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
	backup_storage_need_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'ofield'}))

	class Meta:
		model = Survey
		fields = ['dotr_storage', 'personal_storage', 'storage_section', 'storage_need', 'dotr_storage_others',
		'personal_storage_others', 'storage_need_others', 'dotr_online_storage', 'personal_online_storage',
		'online_storage_need', 'backup_storage', 'backup_storage_others', 'backup_storage_need', 'backup_storage_need_others',
		'storage_comments',]

		widgets = {
			'storage_section': forms.HiddenInput(attrs={'class': 'form-control fieldsize'}),
			'storage_comments': forms.Textarea(attrs={'class': 'form-control'}),
		}

	def __init__(self,*args, **kwargs):
		initial_data = kwargs.get('initial', {})
		initial_data['storage_section'] = 1
		kwargs['initial'] = initial_data
		super(StorageForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_show_labels = False
		self.fields['storage_comments'].required = True
