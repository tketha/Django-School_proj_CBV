from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,DeleteView)
from django.http import HttpResponse
from .models import *

class CBView(View):
    def get(self,request):
        return HttpResponse('<h1>This is general class based View!</h1>')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTion'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'cbv_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = School
    fields = ('name','principle','location')

class SchoolUpdateView(UpdateView):
    fields = ('name','principle')
    model = School

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('cbv_app:list')