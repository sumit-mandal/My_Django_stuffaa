from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,
                                 DetailView,CreateView,UpdateView,
                                 DetailView)
from . import models

class  IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    #ListView changes name of models.School to small letter and ands _list thus returning school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/School_detail.html'
    # DetailView only returns model lowercase

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    models = models.School

class SchoolDeleteView(DeleteView):
    model =models.School
    success_url = reverse_lazy("basic_app:list")
