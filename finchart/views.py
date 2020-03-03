from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, DetailView
from .models import Company, Fstatement
from django.views.generic.list import MultipleObjectMixin

class IndexView(TemplateView):
    template_name = 'finchart/index.html'

    def get_context_data(self, **kwargs):
        fstatement_list = Fstatement.objects.all().order_by('company')
        params = {
            'fstatement_list': fstatement_list,
        }
        return params

class CompanyView(DetailView, MultipleObjectMixin):
    model = Company

    # def get_context_data(self, **kwargs):
    #     company_name = kwargs['object'].name
    #     fstatement_list = Fstatement.objects.filter(company=kwargs['object']).order_by('-fiscal_year')[:4]
    #     params = {
    #         'company_name': company_name,
    #         'fstatement_list': fstatement_list,
    #     }
    #     return params

    paginate_by = 4
    def get_context_data(self, **kwargs):
        object_list = Fstatement.objects.filter(company=kwargs['object']).order_by('-fiscal_year')
        context = super(CompanyView, self).get_context_data(object_list=object_list, **kwargs)

        return context

class FstatementView(DetailView):
    model = Fstatement