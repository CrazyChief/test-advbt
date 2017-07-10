from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseForbidden
from django.urls import reverse
from easycart import BaseItem, BaseCart
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from products.models import Product, ProductVariation
import json
# from .cart import Cart
from .forms import CartAddProductForm
from products.models import Category
from discounts.models import Discount
from discounts.forms import DiscountApplyForm


class Cart(BaseCart):

    # def add(self, pk, quantity=1, **kwargs):
    #     if 'color' in self.request.POST:
    #         color_pk = self.request.POST['color']
    #         color = ProductVariation.objects.filter(pk=color_pk)
    #         # print(self.request.POST['color'])
    #         print(ProductVariation.objects.filter(pk=color_pk))
    #     super(Cart, self).add(pk, quantity, color=color.get().color_value)
    #
    # def list_items_by_color(self):
    #     return self.list_items(sort_key=lambda item: item.color, reverse=False)

    def get_queryset(self, pks):
        return ProductVariation.objects.filter(pk__in=pks)


class CartDetail(TemplateView, FormMixin):
    template_name = "cart/detail.html"
    form_class = DiscountApplyForm

    def get_context_data(self, **kwargs):
        context = super(CartDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.filter(is_active=True)
        context['discount_apply_form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request:
            return HttpResponseForbidden()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        pass

    def get_success_url(self):
        return reverse('cart:detail')






























