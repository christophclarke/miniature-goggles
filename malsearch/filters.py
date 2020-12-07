import django_filters
from django import forms

from malsearch.models import Sample


class SampleFilter(django_filters.FilterSet):
    file_type = django_filters.CharFilter(field_name='scan_results__file_type', lookup_expr='icontains')
    # file_size = django_filters.LookupChoiceFilter(field_name='file_size', field_class=forms.IntegerField, lookup_choices=[
    #     ('exact', 'Equals'),
    #     ('gt', 'Greater than'),
    #     ('lt', 'Less than'),
    # ])

    class Meta:
        model = Sample
        fields = '__all__'
