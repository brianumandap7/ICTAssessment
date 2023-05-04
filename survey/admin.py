from django.contrib import admin
from .models import Survey, office_division, ProfessionalToolsOption, CompetencyScale, ICTTrainingPrograms, CommunicationToolsOption, ProductivityOption, StorageOption, OnlineStorageOption, BackupStorageOption, OnlineOption
# Register your models here.

admin.site.register(Survey)
admin.site.register(office_division)
admin.site.register(ProfessionalToolsOption)
admin.site.register(CompetencyScale)
admin.site.register(ICTTrainingPrograms)
admin.site.register(CommunicationToolsOption)
admin.site.register(ProductivityOption)
admin.site.register(StorageOption)
admin.site.register(OnlineStorageOption)
admin.site.register(BackupStorageOption)
admin.site.register(OnlineOption)

