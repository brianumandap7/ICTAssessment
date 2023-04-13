from time import strptime
from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

class office_division(models.Model):
    office_division_id = models.AutoField(primary_key=True)
    office_division_name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.office_division_name)

class Survey(models.Model):
    survey_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    office_division_name = models.ForeignKey(office_division, on_delete=models.CASCADE, null=True, blank=True, related_name="office_division_names")
    presidential_appointee = models.IntegerField(blank=True, null=True)
    permanent = models.IntegerField(blank=True, null=True)
    coterminus = models.IntegerField(blank=True, null=True)
    jo_cos = models.IntegerField(blank=True, null=True)
    casual_temporary = models.IntegerField(blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    female = models.IntegerField(blank=True, null=True)
    age_20_24 = models.IntegerField(blank=True, null=True)
    age_25_34 = models.IntegerField(blank=True, null=True)
    age_35_44 = models.IntegerField(blank=True, null=True)
    age_45_54 = models.IntegerField(blank=True, null=True)
    age_55_above = models.IntegerField(blank=True, null=True)

    desktop_acer_installed = models.IntegerField(blank=True, null=True)
    desktop_hp_installed = models.IntegerField(blank=True, null=True)
    desktop_lenovo_installed = models.IntegerField(blank=True, null=True)
    desktop_samsung_installed = models.IntegerField(blank=True, null=True)

    mouse_office = models.IntegerField(blank=True, null=True)
    keyboard_office = models.IntegerField(blank=True, null=True)
    tablet_office = models.IntegerField(blank=True, null=True)
    monitor_office = models.IntegerField(blank=True, null=True)
    scanner_office = models.IntegerField(blank=True, null=True)

    laptop_acer_installed = models.IntegerField(blank=True, null=True)
    laptop_hp_installed = models.IntegerField(blank=True, null=True)
    laptop_lenovo_installed = models.IntegerField(blank=True, null=True)
    laptop_samsung_installed = models.IntegerField(blank=True, null=True)

    desktop_personal = models.IntegerField(blank=True, null=True)
    laptop_personal = models.IntegerField(blank=True, null=True)
    tablet_personal = models.IntegerField(blank=True, null=True)
    mouse_personal = models.IntegerField(blank=True, null=True)
    keyboard_personal = models.IntegerField(blank=True, null=True)
    monitor_personal = models.IntegerField(blank=True, null=True)
    scanner_personal = models.IntegerField(blank=True, null=True)

    ordinaryprinter_shared = models.IntegerField(blank=True, null=True)
    coloredprinter_shared = models.IntegerField(blank=True, null=True)
    scanner_shared = models.IntegerField(blank=True, null=True)
    speaker_shared = models.IntegerField(blank=True, null=True)
    tv_shared = models.IntegerField(blank=True, null=True)
    projector_shared = models.IntegerField(blank=True, null=True)
    camera_shared = models.IntegerField(blank=True, null=True)
    microphone_shared = models.IntegerField(blank=True, null=True)
    photocopier_shared = models.IntegerField(blank=True, null=True)

    ordinaryprinter_shared_personal = models.IntegerField(blank=True, null=True)
    coloredprinter_shared_personal = models.IntegerField(blank=True, null=True)
    scanner_shared_personal = models.IntegerField(blank=True, null=True)
    speaker_shared_personal = models.IntegerField(blank=True, null=True)
    tv_shared_personal = models.IntegerField(blank=True, null=True)
    projector_shared_personal = models.IntegerField(blank=True, null=True)
    camera_shared_personal = models.IntegerField(blank=True, null=True)
    microphone_shared_personal = models.IntegerField(blank=True, null=True)
    photocopier_shared_personal = models.IntegerField(blank=True, null=True)

    desktop_need = models.IntegerField(blank=True, null=True)
    laptop_need = models.IntegerField(blank=True, null=True)
    tablet_need = models.IntegerField(blank=True, null=True)
    mouse_need = models.IntegerField(blank=True, null=True)
    keyboard_need = models.IntegerField(blank=True, null=True)
    monitor_need = models.IntegerField(blank=True, null=True)
    ordinaryprinter_need = models.IntegerField(blank=True, null=True)
    coloredprinter_need = models.IntegerField(blank=True, null=True)
    scanner_need = models.IntegerField(blank=True, null=True)
    speaker_need = models.IntegerField(blank=True, null=True)
    tv_need = models.IntegerField(blank=True, null=True)
    projector_need = models.IntegerField(blank=True, null=True)
    camera_need = models.IntegerField(blank=True, null=True)
    microphone_need = models.IntegerField(blank=True, null=True)
    photocopier_need = models.IntegerField(blank=True, null=True)

    hardware_comments = models.CharField(max_length=255, blank=True, null=True)

    privacy_section = models.IntegerField(blank=True, null=True, default = 0)
    demographics_section = models.IntegerField(blank=True, null=True, default = 0)
    hardware_section = models.IntegerField(blank=True, null=True, default = 0)
    software_section = models.IntegerField(blank=True, null=True, default = 0)
    storage_section = models.IntegerField(blank=True, null=True, default = 0)
    competencies_section = models.IntegerField(blank=True, null=True, default = 0)
    trainings_section = models.IntegerField(blank=True, null=True, default = 0)

    def __str__(self):
        return str(self.survey_id)+" "+str(self.user)

