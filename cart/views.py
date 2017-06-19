from django.shortcuts import render, redirect, get_object_or_404
from easycart import BaseItem, BaseCart
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, CreateView, DeleteView
from products.models import Product, ProductVariation
import json
# from .cart import Cart
from .forms import CartAddProductForm
from products.models import Category


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


class CartDetail(TemplateView):
    template_name = "cart/detail.html"

    def get_context_data(self, **kwargs):
        context = super(CartDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.filter(is_active=True)
        return context






























