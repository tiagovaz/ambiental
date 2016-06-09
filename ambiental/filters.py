# -*- coding: utf-8 -*-

import django_filters
from ambientalweb.models import Company, City, Partnership, Neighborhood


class CompanyFilter(django_filters.FilterSet):
    address__city = django_filters.ModelChoiceFilter(label="Cidade", queryset=City.objects.all())
    partnership__description = django_filters.ModelChoiceFilter(label="Parceria", queryset=Partnership.objects.all())
    address__neighborhood__name = django_filters.ModelChoiceFilter(label="Bairro", queryset=Neighborhood.objects.all())

    class Meta:
        model = Company
        fields = [
            'address__neighborhood__name',
            'address__city',
            'partnership__description',
        ]
