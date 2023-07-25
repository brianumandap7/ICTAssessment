from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.admin.views.decorators import staff_member_required
from .views import view_dash

app_name = 'survey'

urlpatterns = [
  path('', login_required(views.view_dash.as_view()), name='dash'),
  path('profile/', login_required(views.profile.as_view()), name='profile'),
  path('demographics/<int:pk>', login_required(views.demographics.as_view()), name='demographics'),
  path('hardware/<int:pk>', login_required(views.hardware.as_view()), name='hardware'),
  path('storage/<int:pk>', login_required(views.Storage.as_view()), name='Storage'),
  path('software/<int:pk>', login_required(views.Software.as_view()), name='Software'),
  path('competencies/<int:pk>', login_required(views.Competencies.as_view()), name='Competencies'),
  path('ict_trainings/<int:pk>', login_required(views.ICTTrainings.as_view()), name='ICTTrainings'),
  path('simple_upload/', staff_member_required(views.simple_upload.as_view()), name='simple_upload'),
  path('export-excel/', views.export_to_excel, name='export_to_excel'),
  path('userinfo/<str:usr>', staff_member_required(views.userinfo), name='userinfo'),
  path('disab/', staff_member_required(views.disab), name='disab'),

  path('act/', staff_member_required(views.act), name='act'),

]	