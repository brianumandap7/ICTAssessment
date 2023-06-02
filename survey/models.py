from time import strptime
from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

class office_division(models.Model):
    office_division_id = models.AutoField(primary_key=True)
    office_division_name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.office_division_name)
    
class ProfessionalToolsOption(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
    

class CompetencyScale(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
    

class ICTTrainingPrograms(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class CommunicationToolsOption(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class ProductivityOption(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class StorageOption(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class OnlineStorageOption(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class BackupStorageOption(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class OnlineOption(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class OfficeLocation(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title

class ConnectionOption(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
    
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
    office_location = models.ManyToManyField(OfficeLocation, blank=True, related_name='office_location')
    pmo_office = models.CharField(max_length=255, blank=True, null=True)

    desktop_acer_installed = models.IntegerField(blank=True, null=True)
    desktop_hp_installed = models.IntegerField(blank=True, null=True)
    desktop_lenovo_installed = models.IntegerField(blank=True, null=True)
    desktop_samsung_installed = models.IntegerField(blank=True, null=True)
    desktop_others_installed = models.IntegerField(blank=True, null=True)

    desktop_acer_personal = models.IntegerField(blank=True, null=True)
    desktop_hp_personal = models.IntegerField(blank=True, null=True)
    desktop_lenovo_personal = models.IntegerField(blank=True, null=True)
    desktop_samsung_personal = models.IntegerField(blank=True, null=True)
    desktop_others_personal = models.IntegerField(blank=True, null=True)

    tablet_acer_installed = models.IntegerField(blank=True, null=True)
    tablet_hp_installed = models.IntegerField(blank=True, null=True)
    tablet_lenovo_installed = models.IntegerField(blank=True, null=True)
    tablet_samsung_installed = models.IntegerField(blank=True, null=True)
    tablet_others_installed = models.IntegerField(blank=True, null=True)

    tablet_acer_personal = models.IntegerField(blank=True, null=True)
    tablet_hp_personal = models.IntegerField(blank=True, null=True)
    tablet_lenovo_personal = models.IntegerField(blank=True, null=True)
    tablet_samsung_personal = models.IntegerField(blank=True, null=True)
    tablet_others_personal = models.IntegerField(blank=True, null=True)

    mouse_acer_installed = models.IntegerField(blank=True, null=True)
    mouse_hp_installed = models.IntegerField(blank=True, null=True)
    mouse_lenovo_installed = models.IntegerField(blank=True, null=True)
    mouse_samsung_installed = models.IntegerField(blank=True, null=True)
    mouse_others_installed = models.IntegerField(blank=True, null=True)

    mouse_acer_personal = models.IntegerField(blank=True, null=True)
    mouse_hp_personal = models.IntegerField(blank=True, null=True)
    mouse_lenovo_personal = models.IntegerField(blank=True, null=True)
    mouse_samsung_personal = models.IntegerField(blank=True, null=True)
    mouse_others_personal = models.IntegerField(blank=True, null=True)

    kb_acer_installed = models.IntegerField(blank=True, null=True)
    kb_hp_installed = models.IntegerField(blank=True, null=True)
    kb_lenovo_installed = models.IntegerField(blank=True, null=True)
    kb_samsung_installed = models.IntegerField(blank=True, null=True)
    kb_others_installed = models.IntegerField(blank=True, null=True)

    kb_acer_personal = models.IntegerField(blank=True, null=True)
    kb_hp_personal = models.IntegerField(blank=True, null=True)
    kb_lenovo_personal = models.IntegerField(blank=True, null=True)
    kb_samsung_personal = models.IntegerField(blank=True, null=True)
    kb_others_personal = models.IntegerField(blank=True, null=True)

    monitor_acer_installed = models.IntegerField(blank=True, null=True)
    monitor_hp_installed = models.IntegerField(blank=True, null=True)
    monitor_lenovo_installed = models.IntegerField(blank=True, null=True)
    monitor_samsung_installed = models.IntegerField(blank=True, null=True)
    monitor_others_installed = models.IntegerField(blank=True, null=True)

    monitor_acer_personal = models.IntegerField(blank=True, null=True)
    monitor_hp_personal = models.IntegerField(blank=True, null=True)
    monitor_lenovo_personal = models.IntegerField(blank=True, null=True)
    monitor_samsung_personal = models.IntegerField(blank=True, null=True)
    monitor_others_personal = models.IntegerField(blank=True, null=True)

    scanner_office = models.IntegerField(blank=True, null=True)

    laptop_acer_installed = models.IntegerField(blank=True, null=True)
    laptop_hp_installed = models.IntegerField(blank=True, null=True)
    laptop_lenovo_installed = models.IntegerField(blank=True, null=True)
    laptop_samsung_installed = models.IntegerField(blank=True, null=True)
    laptop_others_installed = models.IntegerField(blank=True, null=True)


    laptop_acer_personal = models.IntegerField(blank=True, null=True)
    laptop_hp_personal = models.IntegerField(blank=True, null=True)
    laptop_lenovo_personal = models.IntegerField(blank=True, null=True)
    laptop_samsung_personal = models.IntegerField(blank=True, null=True)
    laptop_others_personal = models.IntegerField(blank=True, null=True)

    tablet_personal = models.IntegerField(blank=True, null=True)
    mouse_personal = models.IntegerField(blank=True, null=True)
    keyboard_personal = models.IntegerField(blank=True, null=True)
    monitor_personal = models.IntegerField(blank=True, null=True)
    scanner_personal = models.IntegerField(blank=True, null=True)

    connection_option = models.ManyToManyField(ConnectionOption, blank=True, related_name='connection_option')

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


    dotr_issued_professional_tools_installed = models.ManyToManyField(ProfessionalToolsOption, blank=True, related_name='dotr_issued_professional_tools_installed')
    dotr_issued_professional_tools_installed_others = models.CharField(max_length=255, blank=True, null= True)
    communication_tools_installed = models.ManyToManyField(CommunicationToolsOption, blank=True, related_name='communication_tools_installed')
    communication_tools_installed_others = models.CharField(max_length=255, blank=True, null= True)
    communication_tools_needed = models.ManyToManyField(CommunicationToolsOption, blank=True, related_name='communication_tools_needed')
    communication_tools_needed_others = models.CharField(max_length=255, blank=True, null= True)
    communication_frequent = models.CharField(max_length=255, blank=True, null= True)
    communication_most_needed = models.CharField(max_length=255, blank=True, null= True)
    personal_owned_professional_tools_installed = models.ManyToManyField(ProfessionalToolsOption, blank=True, related_name='personal_owned_professional_tools_installed')
    personal_owned_professional_tools_installed_others = models.CharField(max_length=255, blank=True, null= True)
    professional_tools_needed = models.ManyToManyField(ProfessionalToolsOption, blank=True, related_name='professional_tools_needed')
    professional_tools_needed_others = models.CharField(max_length=255, blank=True, null= True)
    professional_frequent = models.CharField(max_length=255, blank=True, null= True)
    professional_most_needed = models.CharField(max_length=255, blank=True, null= True)
    dotr_issued_productivity_installed = models.ManyToManyField(ProductivityOption, blank=True, related_name='dotr_issued_productivity_installed')
    personal_owned_productivity_installed = models.ManyToManyField(ProductivityOption, blank=True, related_name='personal_owned_productivity_installed')
    dotr_issued_productivity_installed_others = models.CharField(max_length=255, blank=True, null= True)
    personal_owned_productivity_installed_others = models.CharField(max_length=255, blank=True, null= True)
    productivity_needed = models.ManyToManyField(ProductivityOption, blank=True, related_name='productivity_needed')
    productivity_needed_others = models.CharField(max_length=255, blank=True, null= True)
    productivity_frequent = models.CharField(max_length=255, blank=True, null= True)
    productivity_most_needed = models.CharField(max_length=255, blank=True, null= True)

    software_comments = models.CharField(max_length=255, blank=True, null=True)

    dotr_storage = models.ManyToManyField(StorageOption, blank=True, related_name='dotr_storage')
    dotr_sotrage_others = models.CharField(max_length=255, blank=True, null= True)
    personal_storage = models.ManyToManyField(StorageOption, blank=True, related_name='personal_storage')
    personal_storage_others = models.CharField(max_length=255, blank=True, null= True)
    storage_need = models.ManyToManyField(StorageOption, blank=True, related_name='storage_need')
    storage_need_others = models.CharField(max_length=255, blank=True, null= True)

    dotr_online_storage = models.ManyToManyField(OnlineStorageOption, blank=True, related_name='dotr_online_storage')
    personal_online_storage = models.ManyToManyField(OnlineStorageOption, blank=True, related_name='personal_online_storage')
    online_storage_need = models.ManyToManyField(OnlineStorageOption, blank=True, related_name='online_storage_need')

    backup_storage = models.ManyToManyField(BackupStorageOption, blank=True, related_name='backup_storage')
    backup_storage_others = models.CharField(max_length=255, blank=True, null= True)

    backup_storage_need = models.ManyToManyField(BackupStorageOption, blank=True, related_name='backup_storage_need')
    backup_storage_need_others = models.CharField(max_length=255, blank=True, null= True)

    storage_comments = models.CharField(max_length=255, blank=True, null=True)

    ict_trainings_taken = models.ManyToManyField(ICTTrainingPrograms, blank=True, related_name='ict_trainings_taken')
    ict_trainings_taken_others = models.CharField(max_length=255, blank=True, null=True)

    ict_trainings_interests = models.ManyToManyField(ICTTrainingPrograms, blank=True, related_name='ict_trainings_interests')
    ict_trainings_interests_others = models.CharField(max_length=255, blank=True, null=True)

    ict_training_comments = models.CharField(max_length=255, blank=True, null=True)


    turning_on_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='turning_on_familiar')
    network_cable_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='network_cable_familiar')
    network_wifi_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='network_wifi_familiar')
    usb_printer_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='usb_printer_familiar')
    wireless_printer_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='wireless_printer_familiar')

    saving_files_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='saving_files_familiar')
    creating_folders_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='creating_and_naming_folders_familiar')
    copying_deleting_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='copying_and_deleting_familiar')
    installing_software = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='installing_software')
    file_types_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='file_types_familiar')
    unzip_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='unzip_familiar')
    file_search_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='file_search_familiar')
    connect_device_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='connect_device_familiar')
    
    access_email_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='access_email_familiar')
    sending_email_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='sending_email_familiar')
    add_attachments_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='add_attachments_familiar')
    add_signatures_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='add_signatures_familiar')
    mailing_list_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='mailing_list_familiar')

    gmail_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='gmail_familiar')
    meet_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='meet_familiar')
    calendar_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='calendar_familiar')
    drive_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='drive_familiar')
    docs_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='docs_familiar')
    sheets_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='sheets_familiar')
    sliders_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='sliders_familiar')
    forms_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='forms_familiar')
    sites_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='sites_familiar')
    keep_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='keep_familiar')

    outlook_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='outlook_familiar')
    teams_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='teams_familiar')
    onedrive_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='onedrive_familiar')
    word_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='word_familiar')
    excel_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='excel_familiar')
    ppt_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='ppt_familiar')
    forms2_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='forms2_familiar')
    sharepoint_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='sharepoint_familiar')
    onenote_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='onenote_familiar')
    powerbi_familiar = models.ForeignKey(CompetencyScale, on_delete=models.CASCADE, null=True, blank=True, related_name='powerbi_familiar')
    
    online_options = models.ForeignKey(OnlineOption, on_delete=models.CASCADE, null=True, blank=True, related_name='online_options')
    competencies_comments = models.CharField(max_length=255, blank=True, null=True)

    submitted = models.IntegerField(blank=True, null=True, default = 0)
    def __str__(self):
        return str(self.survey_id)+" "+str(self.user)

