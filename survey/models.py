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

    desktop_acer_installed = models.IntegerField(blank=True, null=True)
    desktop_hp_installed = models.IntegerField(blank=True, null=True)
    desktop_lenovo_installed = models.IntegerField(blank=True, null=True)
    desktop_samsung_installed = models.IntegerField(blank=True, null=True)
    mouse_installed = models.IntegerField(blank=True, null=True)
    keyboardesktop_hp_installed = models.IntegerField(blank=True, null=True)

    privacy_section = models.IntegerField(blank=True, null=True, default = 0)
    demographics_section = models.IntegerField(blank=True, null=True, default = 0)
    hardware_section = models.IntegerField(blank=True, null=True, default = 0)
    software_section = models.IntegerField(blank=True, null=True, default = 0)
    storage_section = models.IntegerField(blank=True, null=True, default = 0)
    competencies_section = models.IntegerField(blank=True, null=True, default = 0)
    trainings_section = models.IntegerField(blank=True, null=True, default = 0)

    def __str__(self):
        return str(self.survey_id)+" "+str(self.user)

