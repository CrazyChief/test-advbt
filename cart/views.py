from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseForbidden
from django.urls import reverse
from easycart import BaseItem, BaseCart
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.conf import settings
from products.models import Product, ProductVariation
import json
# from .cart import Cart
from .forms import CartAddProductForm
from products.models import Category
from discounts.models import Discount
from discounts.forms import DiscountApplyForm


class Cart(BaseCart):

    def get_queryset(self, pks):
        return ProductVariation.objects.filter(pk__in=pks)


class CartDetail(TemplateView):
    template_name = "cart/detail.html"
    # form_class = DiscountApplyForm

    def get_context_data(self, **kwargs):
        context = super(CartDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.filter(is_active=True)
        # context['discount_apply_form'] = self.get_form()
        return context

    # def post(self, request, *args, **kwargs):
    #     if not request:
    #         return HttpResponseForbidden()
    #     form = self.get_form()
    #
    #     if form.is_valid():
    #         now = timezone.now()
    #         code = form.cleaned_data['discount_code']
    #         try:
    #             discount = Discount.objects.get(discount_code__iexact=code, discount_start_period__gte=now,
    #                                             discount_end_period__lte=now)
    #             request.session['discount_id'] = discount.id
    #         except Discount.DoesNotExist:
    #             request.session['discount_id'] = None
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def get_success_url(self):
        return reverse('cart:detail')






























