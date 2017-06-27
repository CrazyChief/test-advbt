import django_filters
from django_filters import widgets as wg

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models import Q
from django import forms
from .models import Product, ProductVariation, SubCategory


# def sub_categor(request):
#     if request is None:
#         return SubCategory.objects.none()
#
#     sub_category = request.category.subcategory_set.filter(category__pk=request.category.pk)
#     return sub_category

# STATUS_CHOICES = (
#     (0, 'Regular'),
#     (1, 'Manager'),
#     (2, 'Admin'),
# )


class ProductFilter(django_filters.FilterSet):
    # q = django_filters.
    # sub_categories = django_filters.ModelMultipleChoiceFilter(name='sub_categories', queryset=sub_categor)
    # sub_categories = django_filters.MultipleChoiceFilter(name='sub_categories', lookup_expr='contains', widget=forms.CheckboxSelectMultiple())
    sub_categories = django_filters.AllValuesFilter(
        name='sub_categories',
        # method='sub_categories_custom_filter',
        widget=wg.LinkWidget,
        lookup_expr='contains',
    )
    # price = django_filters.RangeFilter(label='price')

    class Meta:
        model = Product
        fields = [
            'category',
            'sub_categories',
            # 'title',
        ]

        # filter_overrides = {
        #     models.ManyToManyField: {
        #         'filter_class': django_filters.MultipleChoiceFilter,
        #         'extra': lambda f: {
        #             'widget': forms.CheckboxSelectMultiple,
        #         },
        #     },
        # }

    # def filter_sub(self, queryset, name, value):
    #     # construct the full lookup expression.
    #     # alternatively, it may not be necessary to construct the lookup.
    #     return queryset.filter(sub_categories__category__pk=value)

    # @property
    # def qs(self):
    #     parent = super(ProductFilter, self).qs
    #     category = getattr(self.request, 'products_list', None)
    #     print("Request: %s" % self.request)
    #     print("Category: %s" % category)
    #     return parent.filter(sub_categories__category__pk=1)




