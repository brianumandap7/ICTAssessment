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

from .models import Survey, office_division, CommunicationToolsOption, ProductivityOption, StorageOption, OnlineStorageOption, BackupStorageOption, OnlineOption

from .forms import demographicsform, hardwareform, SoftwareForm, CompetenciesForm, ICTTrainingsForm, StorageForm

from django.urls import reverse_lazy
from .resources import PersonResource
from tablib import Dataset
# Create your views here.

class view_dash(View):
    template_name = 'survey/survey.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        query = {
            'check_user': Survey.objects.filter(user=request.user),
            'sec': 1,
        }
        return render(request, self.template_name, query)

    def post(self, request, *args, **kwargs):
        db = Survey()
        if request.POST.get('ia'):
            db.privacy_section = 1
            db.user = request.user
        db.save()

        return HttpResponseRedirect('/survey/')

class simple_upload(View):
    template_name = 'survey/upload.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        query = {
            'check_user': Survey.objects.filter(user=request.user),
        }
        return render(request, self.template_name, query)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            person_resource = PersonResource()
            db = Survey()
            dataset = Dataset()

            new_person = request.FILES['myfile']

            if not new_person.name.endswith('xlsx'):
                messages.info(request, 'wrong file format')
                return render (request, '/')
            imported_data = dataset.load(new_person.read(),format = 'xlsx')
            for data in imported_data:
                db = User()
                db.username = data[1]
                pw = data[2]
                db.set_password(pw)
                db.email = data[3]
                db.first_name = data[4]
                db.last_name = data[5]
                db.is_staff = data[6]
                db.save()

            return HttpResponseRedirect('/survey/')
        

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
        context['check_user'] = Survey.objects.filter(user = self.request.user)
        context['sec'] = 2
        context['pk'] = self.kwargs.get('pk')

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
        context['check_user'] = Survey.objects.filter(user = self.request.user)
        context['sec'] = 3
        context['pk'] = self.kwargs.get('pk')

        return context

class Software(LoginRequiredMixin, UpdateView):
    model = Survey
    form_class = SoftwareForm
    template_name = 'survey/software.html'
    success_url = reverse_lazy('survey:dash')
    
    def get_context_data(self, **kwargs):
        context = super(Software, self).get_context_data(**kwargs)
        context['title'] = 'Software'
        context['check_user'] = Survey.objects.filter(user = self.request.user)
        context['sec'] = 4
        context['pk'] = self.kwargs.get('pk')
        return context

class Storage(LoginRequiredMixin, UpdateView):
    model = Survey
    form_class = StorageForm
    template_name = 'survey/storage.html'
    success_url = reverse_lazy('survey:dash')
    
    def get_context_data(self, **kwargs):
        context = super(Storage, self).get_context_data(**kwargs)
        context['title'] = 'Storage'
        context['check_user'] = Survey.objects.filter(user = self.request.user)
        context['sec'] = 5
        context['pk'] = self.kwargs.get('pk')
        return context

class Competencies(LoginRequiredMixin, UpdateView):
    model = Survey
    form_class = CompetenciesForm
    template_name = 'survey/competencies.html'
    success_url = reverse_lazy('survey:dash')

    def get_context_data(self, **kwargs):
        context = super(Competencies, self).get_context_data(**kwargs)
        context['title'] = 'Competencies'
        context['check_user'] = Survey.objects.filter(user = self.request.user)
        context['sec'] = 6
        context['pk'] = self.kwargs.get('pk')
        return context


class ICTTrainings(LoginRequiredMixin, UpdateView):
    model = Survey
    form_class = ICTTrainingsForm
    template_name = 'survey/ict_trainings.html'
    success_url = reverse_lazy('survey:dash')

    def get_context_data(self, **kwargs):
        context = super(ICTTrainings, self).get_context_data(**kwargs)
        context['title'] = 'ICT Trainings'
        context['check_user'] = Survey.objects.filter(user = self.request.user)
        context['sec'] = 7
        context['pk'] = self.kwargs.get('pk')
        return context


