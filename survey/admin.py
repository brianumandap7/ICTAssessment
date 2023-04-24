from django.contrib import admin
from .models import Survey, office_division, ProfessionalToolsOption, CompetencyScale, ICTTrainingPrograms
# Register your models here.

admin.site.register(Survey)
admin.site.register(office_division)
admin.site.register(ProfessionalToolsOption)
admin.site.register(CompetencyScale)
admin.site.register(ICTTrainingPrograms)
