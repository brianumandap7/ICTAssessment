from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.http import JsonResponse, HttpResponse

from django.core import serializers
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, F, Max, Count
from django.db import IntegrityError
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.db.models import Q
from datetime import date, timedelta, datetime
from django.db.models.functions import Extract, Now, Trunc
from django.db import models
from django.db.models import Sum
# from .visualizations import S_Curve_Project_Visualization, truncate

from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Survey

from .forms import demographicsform, hardwareform

from django.urls import reverse_lazy
# Create your views here.

class view_dash(View):
    template_name = 'survey/survey.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        query = {
            'check_user': Survey.objects.filter(user=request.user),
        }
        return render(request, self.template_name, query)

    def post(self, request, *args, **kwargs):
        db = Survey()
        if request.POST.get('ia'):
            db.privacy_section = 1
            db.user = request.user
        db.save()

        return HttpResponseRedirect('/survey/')

class demographics(UpdateView):
	model = Survey
	form_class = demographicsform
	template_name = 'survey/demographics.html'
	success_url = reverse_lazy('survey:dash')

	def get_context_data(self, **kwargs):
		context = super(demographics, self).get_context_data(**kwargs)
		context['title'] = 'Demographics'

		return context

class profile(View):
	template_name = 'survey/profile.html'


	def get(self, request, *args, **kwargs):
		query = {
			'check_user': Survey.objects.filter(user=request.user),
		}

		return render(request, self.template_name, query)

class hardware(UpdateView):
	model = Survey
	form_class = hardwareform
	template_name = 'survey/hardware.html'
	success_url = reverse_lazy('survey:dash')

	def get_context_data(self, **kwargs):
		context = super(hardware, self).get_context_data(**kwargs)
		context['title'] = 'Hardware'
		context['qt'] = 'Desktop Computers:'
		context['qs'] = 'Identify the number of DOTr-issued Desktop Computers in your division/office:'
		context['q1'] = 'Please indicate the number of Desktop Computers per brand:'

		context['qt2'] = 'Laptop Computers:'
		context['qs2'] = 'Identify the number of DOTr-issued Laptop Computers in your division/office:'
		context['q2'] = 'Please indicate the number of Laptop Computers per brand:'

		context['qt3'] = 'Tablets'
		context['qs3'] = 'Identify the number of DOTr-issued Laptop Computers in your division/office:'

		return context




