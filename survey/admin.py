from django.contrib import admin
from .models import Survey, office_division, ProfessionalToolsOption, CompetencyScale, ICTTrainingPrograms, CommunicationToolsOption, ProductivityOption, StorageOption, OnlineStorageOption, BackupStorageOption, OnlineOption
from import_export.admin import ImportExportModelAdmin, ExportActionMixin

class exportSurvey(ExportActionMixin, admin.ModelAdmin):
	pass
# Register your models here.

admin.site.register(Survey, exportSurvey)
admin.site.register(office_division, exportSurvey)
admin.site.register(ProfessionalToolsOption, exportSurvey)
admin.site.register(CompetencyScale, exportSurvey)
admin.site.register(ICTTrainingPrograms, exportSurvey)
admin.site.register(CommunicationToolsOption, exportSurvey)
admin.site.register(ProductivityOption, exportSurvey)
admin.site.register(StorageOption, exportSurvey)
admin.site.register(OnlineStorageOption, exportSurvey)
admin.site.register(BackupStorageOption, exportSurvey)
admin.site.register(OnlineOption, exportSurvey)

