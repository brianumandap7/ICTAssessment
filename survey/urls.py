from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'survey'

urlpatterns = [
  path('', login_required(views.view_dash.as_view()), name='dash'),
  path('profile/', login_required(views.profile.as_view()), name='profile'),
  path('demographics/<int:pk>', login_required(views.demographics.as_view()), name='demographics'),
  path('hardware/<int:pk>', login_required(views.hardware.as_view()), name='hardware'),
]	