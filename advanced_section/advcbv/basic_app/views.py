from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
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
