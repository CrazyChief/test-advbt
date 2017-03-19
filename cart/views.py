from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, CreateView, DeleteView
from products.models import ProductVariation
from .cart import Cart
from .forms import CartAddProductForm


# @require_POST
class CartAdd(CreateView):
    pass


class CartDelete(DeleteView):
    pass


class CartDetail(TemplateView):
    template_name = 'cart/detail.html'

    def get(self, request, *args, **kwargs):
        self.cart = self.get_cart(request)

    def get_cart(self, request):
        cart = Cart(request)
        return cart































