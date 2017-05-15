from django.shortcuts import render, redirect, get_object_or_404
from easycart import BaseCart
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, CreateView, DeleteView
from products.models import Product, ProductVariation
# from .cart import Cart
from .forms import CartAddProductForm


class Cart(BaseCart):

    def get_queryset(self, pks):
        return Product.objects.filter(pk__in=pks)


class CartDetail(TemplateView):
    template_name = "cart/detail.html"






























