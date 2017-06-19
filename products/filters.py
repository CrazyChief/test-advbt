import django_filters

from django.utils.translation import ugettext_lazy as _
from .models import Product, ProductVariation, SubCategory


class ProductFilter(django_filters.FilterSet):
    sub_categories = django_filters.MultipleChoiceFilter(name='sub_category', lookup_expr='exact')

    class Meta:
        model = SubCategory
        fields = ['title',]




