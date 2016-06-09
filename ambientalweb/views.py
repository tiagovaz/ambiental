from django.views import generic

from ambiental.filters import CompanyFilter
from ambientalweb.models import Company


class CompanyList(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'companies'
    model = Company

    def get_queryset(self):
        return CompanyFilter(self.request.GET, queryset=Company.objects.all())

    def dispatch(self, *args, **kwargs):
        return super(CompanyList, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CompanyList, self).get_context_data(**kwargs)

        all_companies = CompanyFilter(self.request.GET, queryset=Company.objects.all())
        context['view'] = "companies"
        context['form'] = all_companies.form

        return context
